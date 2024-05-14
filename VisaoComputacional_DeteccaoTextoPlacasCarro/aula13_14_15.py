# Aula 13 - Contraste
import cv2
import numpy as np
from skimage.segmentation import clear_border
import pytesseract as pt
import re

# Import, grayscale
image = cv2.imread("imagens/placa_carro3.jpg")
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("grayscale", grayscale)

# Black Hat
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 13))
black_hat = cv2.morphologyEx(grayscale, cv2.MORPH_BLACKHAT, rect_kernel)
# cv2.imshow("black hat", black_hat)

# Sobel
# 32 bits do tipo float
sobel_x = cv2.Sobel(
    black_hat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=1
)  # Usamos sobel_x por conta da placa ter uma largura maior que a altura
sobel_x = np.absolute(sobel_x)
sobel_x = sobel_x.astype("uint8")
# cv2.imshow("sobel x", sobel_x)

# # Desafio - Sobel Y
# sobel_y = cv2.Sobel(black_hat, ddepth= cv2.CV_32F, dx = 0, dy = 1, ksize= 1)
# sobel_y = np.absolute(sobel_y)
# sobel_y = sobel_y.astype('uint8')
# cv2.imshow('sobel y', sobel_y)

# Aula 14 - Mascara
# Gaussian Blur + Closing
sobel_x = cv2.GaussianBlur(sobel_x, (5, 5), 0)
sobel_x = cv2.morphologyEx(sobel_x, cv2.MORPH_CLOSE, rect_kernel)
# cv2.imshow("gaussian blur + closing", sobel_x)
# Otsu
value, thresh_otsu = cv2.threshold(sobel_x, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# cv2.imshow("otsu", thresh_otsu)
# Erosion
square_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
erosion = cv2.erode(thresh_otsu, square_kernel, iterations=2)  # double erosion
# Dilatation
dilatation = cv2.dilate(erosion, square_kernel, iterations=2) # double dilatation
cv2.imshow('erosion + dilatation', dilatation)

# Closing (grayscale image)
closing = cv2.morphologyEx(grayscale, cv2.MORPH_CLOSE, square_kernel)
value, mask = cv2.threshold(closing, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('mask', mask)

# Threshold
bitwise_and = cv2.bitwise_and(dilatation, dilatation, mask = mask)
dilatation2 = cv2.dilate(bitwise_and, square_kernel, iterations= 2)
erosion2 = cv2.erode(dilatation2, square_kernel)
cv2.imshow('erosion2', erosion2)

# Aula 15 - Deteccao de caracteres
clear = clear_border(erosion2)
cv2.imshow('clear border', clear)

contours, hierarchy = cv2.findContours(clear, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse=True)[:10]
print(contours)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    proportion = float(w)/h
    if proportion >= 3 and proportion <= 3.5:
        license_plate = grayscale[y:y+h, x:x+w]
        value, interest_region = cv2.threshold(license_plate, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        interest_region = clear_border(interest_region)
        cv2.imshow('plate', license_plate)
        cv2.imshow('interest region', interest_region)

# Se atentar ao nome de usuario em --tessdata-dir
text = pt.image_to_string(interest_region, lang='por',  config='--tessdata-dir /home/lanzo/tessdata --psm 6')
print(text)

extracted_text = re.search('\w{3}\d{1}\w{1}\d{2}', text)
print(extracted_text)
print(extracted_text.group(0))
print('Texto Detectado:', extracted_text.group(0))
cv2.imwrite('imagem3_apos_pre_processamento.png', interest_region)

cv2.waitKey()
cv2.destroyAllWindows()