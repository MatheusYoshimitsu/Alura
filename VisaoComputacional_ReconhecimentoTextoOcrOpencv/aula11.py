import re
import cv2
import pytesseract as pt
from pytesseract import Output
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

default_data = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'

copy_img = rgb.copy()
for i in range(0, len(result['text'])):
    confidence = int(result['conf'][i])
    if confidence

cv2.waitKey()
cv2.destroyAllWindows()