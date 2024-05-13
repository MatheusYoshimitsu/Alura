import cv2
import pytesseract as pt
import re

# Import, grayscale
image = cv2.imread('imagens/placa_carro1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny
bordas = cv2.Canny(gray, 100, 200)
cv2.imshow('canny', bordas)

# Contorno
contornos, hierarquia = cv2.findContours(bordas, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contorno in contornos:
    epsilon = 0.02 * cv2.arcLength(contorno, True)
    aproximacao = cv2.approxPolyDP(contorno, epsilon, True)
    if cv2.isContourConvex(aproximacao) and len(aproximacao) == 4:
        localizacao = aproximacao
        break

x, y, w, h = cv2.boundingRect(localizacao)
# print(x, y, w, h)
placa = gray[y:y+h, x:x+w]
cv2.imshow('placa', placa)

# Otsu
valor, lim_otsu = cv2.threshold(placa, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('otsu', lim_otsu)
# Erosao
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,4))
erosao = cv2.erode(lim_otsu, kernel)
cv2.imshow('erosao', erosao)
# Tesseract
config = '--tessdata-dir /home/lanzo/tessdata --psm 6'
lang = 'por'
text = pt.image_to_string(erosao, lang, config)
# print(text)

# Apenas placas MERCOSUL!
extracted_text = re.search('\w{3}\d{1}\w{1}\d{2}', text)
#print(extracted_text)
print('Texto Detectado:', extracted_text.group(0))
cv2.imwrite('imagem1_apos_5_tecnicas_pre_processamento.png', erosao)

cv2.waitKey()
cv2.destroyAllWindows()