# Aula 12 - Aplicacoes em outros cenarios
import cv2
import pytesseract as pt
import re

# Import, grayscale, show
image = cv2.imread('imagens/placa_carro2.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', image)

# Canny Edge Detection
edges = cv2.Canny(image, 100, 200)
cv2.imshow('canny', edges)

# Contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse=True)[:10] # Recebe apenas os 10 maiores contornos

for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    aprox = cv2.approxPolyDP(contour, epsilon, True)
    if cv2.isContourConvex(aprox) and len(aprox) == 4:
        localization = aprox
        break

print(localization)

# Crop to license_plate
x, y, w, h = cv2.boundingRect(localization)
license_plate = image[y:y+h, x:x+w]
cv2.imshow('license_plate', license_plate) 

# Otsu
value, thresh_otsu = cv2.threshold(license_plate, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('otsu', thresh_otsu)
# This is an optional step, the image does not have noises in its writings
# Erosion
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,4))
erosion = cv2.erode(thresh_otsu, kernel)
cv2.imshow('erosion', erosion)

# Tesseract
config = '--tessdata-dir /home/lanzo/tessdata --psm 6'
text = pt.image_to_string(thresh_otsu, 'por', config)
print(text)

# Regex
extracted_text = re.search('\w{3}\d{1}\w{1}\d{2}', text)
print(extracted_text)
print(extracted_text.group(0))
print('Texto Detectado:', extracted_text.group(0))
cv2.imwrite('imagem2_apos_pre_processamento.png', erosion)

cv2.waitKey()
cv2.destroyAllWindows()