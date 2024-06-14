import re
import cv2
import pytesseract as pt
from pytesseract import Output
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import json
# import pandas as pd

img = cv2.imread('CursoAlura-TextRecognize/Imagens/Aula4-tabela_teste.png')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb', rgb)

config_tesseract = '--tessdata-dir /home/lanzo/tessdata'

result = pt.image_to_data(rgb, config=config_tesseract, lang='por', output_type=Output.DICT)

# Deixando num formato parecido com JSON
ordered_keys = ['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text']
ordered_result = [dict(zip(ordered_keys, row)) for row in zip(*(result[key] for key in ordered_keys))]
json_result = json.dumps(ordered_result, indent=4)
print(json_result)

# # Usando pandas para deixar mais legivel
# data_frame = pd.DataFrame(result)
# columns = ['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text']
# data_frame = data_frame[columns]
# print(data_frame)

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

# ^ marca o inicio da string
# (0[1-9]|[12][0-9]|3[01]) significa (0 seguido de 1-9) ou ((1 ou 2) seguido de 0-9) ou (3 seguido de 0 ou 1)
# (0[1-9]|1[012]) significa (0 seguido de 1-9) ou (1 seguido de 0 ou 1 ou 2)
# (19|20)\d\d$ significa 19 ou 20 seguido por dois digitos quaisquer
# $ marca o final da string
date_format = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
copy_img = rgb.copy()
dates = []

for i in range(0, len(result['text'])):
    confidence = int(result['conf'][i])
    if confidence > min_conf:
        text = result['text'][i]
        if re.match(date_format, text):
            x, y, img = bounding_box(result, copy_img, (0, 0, 255)) # Deixa a caixa em vermelho Esta em BGR, nao RGB
            copy_img = write_text(text, x, y, copy_img, font, 12)
            dates.append(text)
        else:
            x, y, copy_img = bounding_box(result, copy_img)

print(dates)

cv2.imshow('Copy Image', copy_img)

cv2.waitKey()
cv2.destroyAllWindows()