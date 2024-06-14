# Aula 03 em anotacoes.md
# Exercicio - Aplicando o PSM
import cv2
import pytesseract as pt

img = cv2.imread('CursoAlura-TextRecognize/Atividades/Aula2-Nota_Fiscal.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

config_tesseract = '--tessdata-dir /home/lanzo/tessdata --psm 4' # Resposta correta, porem o output nao esta correto
text = pt.image_to_string(rgb, lang='por', config=config_tesseract)
print(text)