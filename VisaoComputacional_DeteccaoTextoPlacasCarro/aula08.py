# Aula 8 - Outras transformacoes
import cv2;
import pytesseract as pt

# Import
image = cv2.imread('imagens/placa_carro1.png')
# Grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Otsu
valor, lim_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('Limiar de Otsu', lim_otsu)

# Kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# Gradiente
gradiente = cv2.morphologyEx(lim_otsu, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Transformacao Gradiente', gradiente)
# Top Hat
kernel_hat = cv2.getStructuringElement(cv2.MORPH_RECT, (40,13))
top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel_hat) # pode-se usar outros tipos parametros (ex: otsu + kernel (5,5))
cv2.imshow('Transformacao Top Hat', top_hat)
# Black Hat
black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel_hat)
cv2.imshow('Transformacao Black Hat', black_hat)

# Erosao (bom resultado)
erosao = cv2.erode(lim_otsu, kernel)
cv2.imshow('Erosao', erosao)

# Tesseract
config_tess = '--tessdata-dir /home/lanzo/tessdata --psm 6'
lang = 'por'
text = pt.image_to_string(erosao, lang, config_tess)
print(text)

cv2.waitKey()
cv2.destroyAllWindows()