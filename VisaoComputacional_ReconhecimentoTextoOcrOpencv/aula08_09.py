# Aula 08 - Fontes
import cv2
import numpy as np
import pytesseract as pt
from pytesseract import Output
from PIL import ImageFont, ImageDraw, Image
import os

img = cv2.imread("CursoAlura-TextRecognize/Imagens/Aula1-ocr.png")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", rgb)

config_tesseract = "--tessdata-dir /home/lanzo/tessdata"
result = pt.image_to_data(rgb, config=config_tesseract, lang="por", output_type=Output.DICT)
print(result)

min_conf = 40
font = 'CursoAlura-TextRecognize/Imagens/calibri.ttf'

# Aula 09 - Funcao para fontes

def bounding_box(result, img, color = (255, 100, 0)):
    x = result['left'][i]
    y = result['top'][i]
    w = result['width'][i]
    h = result['height'][i]

    cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)

    return x, y, img

print(len(result['text']))

# 1. Passa a imagem (array), transforma para pil, escreve texto com a fonte calibri. 
# 2. Pega a imagem pil e a transforma em array novamente
# Embora seja um processo mais demorado, este metodo tem melhor identificacao de caracteres especiais 
def write_text(text, x, y, img, font, text_size = 32):
    font = ImageFont.truetype(font, text_size)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x, y - text_size), text, font = font)
    img = np.array(img_pil)
    return img

copy_img = rgb.copy()
for i in range(len(result['text'])):
    confidence = int(result['conf'][i])
    if confidence > min_conf:
        x, y, img = bounding_box(result, copy_img)

        text = result['text'][i]
        copy_img = write_text(text, x, y, copy_img, font)

cv2.imshow('COPY IMG', copy_img)

# Salvando a imagem
os.makedirs('images_tesseract', exist_ok=True)
logo_tesseract = 'images_tesseract/logo_tesseract.png'
cv2.imwrite(logo_tesseract, copy_img)

cv2.waitKey()
cv2.destroyAllWindows()