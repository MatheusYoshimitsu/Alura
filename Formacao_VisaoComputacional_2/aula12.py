# Aula 11 - Cenarios Naturais
import cv2
import pytesseract as pt
from pytesseract import Output
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import json

img = cv2.imread('CursoAlura-TextRecognize/Imagens/Aula4-caneca2.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

config_tesseract = '--tessdata-dir /home/lanzo/tessdata --psm 6'
result = pt.image_to_data(rgb, lang='por', config=config_tesseract, output_type=Output.DICT)
# print(result)
min_conf = 40
font = 'CursoAlura-TextRecognize/Imagens/calibri.ttf'

def bounding_box(result, img, color = (255, 100, 0)):
    x = result['left'][i]
    y = result['top'][i]
    w = result['width'][i]
    h = result['height'][i]

    cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)

    return x, y, img

def write_text(text, x, y, img, font, text_size = 32):
    font = ImageFont.truetype(font, text_size)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x, y - text_size), text, font = font)
    img = np.array(img_pil)
    return img

copy_img = rgb.copy()

# Deixando num formato parecido com JSON
ordered_keys = ['conf', 'text']
ordered_result = [dict(zip(ordered_keys, row)) for row in zip(*(result[key] for key in ordered_keys))]
json_result = json.dumps(ordered_result, indent=4)
print(json_result)

# Pode-se perceber que aumentar a confianca nao traria sucesso, ja que perderiamos VP e ainda haveriam FP
# Uma possivel solucao seria excluir os caracteres que tenham FP, mas neste exemplo, a palavra 'e' sera perdida. 
# Como o curso nao abrange pre processamento, essa opcao  foi escolhida

# Opiniao pessoal: solucao ruim
# Desafio pessoal: aplicar pre processamento e retirar os FP sem perder VP

# Prosseguindo a aula:
for i in range(0, len(result['text'])):
    confidence = int(result['conf'][i])
    if confidence > min_conf:
        text = result['text'][i]
        if not text.isspace() and len(text) > 1:
            x, y, img = bounding_box(result, copy_img)
            copy_img = write_text(text, x, y, copy_img, font)
cv2.imshow('Copy Image', copy_img)

cv2.waitKey()
cv2.destroyAllWindows()