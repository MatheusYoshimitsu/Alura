# Exercicio 2 - Utilizando Regex

import cv2
import pytesseract as pt
import numpy as np
import re
from PIL import Image, ImageDraw, ImageFont
from pytesseract import Output

img = cv2.imread('CursoAlura-TextRecognize/Atividades/Aula4_cotacao.png')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

config_tesseract = '--tessdata-dir /home/lanzo/tessdata'

result = pt.image_to_data(rgb, config=config_tesseract, lang='por', output_type=Output.DICT)

min_conf = 25
font = 'CursoAlura-TextRecognize/Imagens/calibri.ttf'

def bounding_box(result, img, color = (255,100,0)):
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

hour_format = '^[012]\d:[0-5]\d:00.0$'
info = []
copy_img = rgb.copy()

for i in range(0, len(result['text'])):
    confidence = int(result['conf'][i])
    if confidence > min_conf:
        text = result['text'][i]
        if re.match(hour_format, text):
            x, y, img = bounding_box(result, copy_img, (0,0,255)) # Red box
            copy_img = write_text(text, x, y, copy_img, font, 12)
            info.append(text)
        else:
            x, y, copy_img = bounding_box(result, copy_img)

cv2.imshow('Copy Image', copy_img)

cv2.waitKey()
cv2.destroyAllWindows()