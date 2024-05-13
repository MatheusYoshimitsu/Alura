# Aula 6 - Erosao e dilatacao
import cv2

# Importa a imagem
image = cv2.imread('imagens/placa_carro1.png')
# Transforma em cinza
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Aplica a limiarizacao de Otsu
valor, lim_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('image otsu', lim_otsu)

# Aplicando erosao (expandindo pixels pretos/diminuindo pixels brancos)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
erosao = cv2.erode(lim_otsu, kernel)
cv2.imshow('image erosao', erosao)

# Aplicando a dilatacao (expandindo pixels brancos/diminuindo pixels pretos)
dilatacao = cv2.dilate(lim_otsu, kernel);
cv2.imshow('image dilate', dilatacao)

cv2.waitKey()
cv2.destroyAllWindows()