# Aula 7 - Abertura e Fechamento
import cv2

# Importa a imagem
image = cv2.imread('imagens/placa_carro1.png')
# Transforma em cinza
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Aplica a limiarizacao de Otsu
valor, lim_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('image otsu', lim_otsu)

# Define o kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# Aplicando abertura
abertura = cv2.morphologyEx(lim_otsu, cv2.MORPH_OPEN, kernel)
cv2.imshow('image abertura', abertura)
# Aplicando fechamento
fechamento = cv2.morphologyEx(lim_otsu, cv2.MORPH_CLOSE, kernel)
cv2.imshow('image fechamento', fechamento)

cv2.waitKey()
cv2.destroyAllWindows()