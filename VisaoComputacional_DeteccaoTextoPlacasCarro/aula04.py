# Aula 4: Limiarizacao adaptativa
import cv2

image = cv2.imread('imagens/placa_carro1.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# PELA MEDIA
# origem, valor maximo, limiarizacao pela media, binarizacao, vizinhanca de 11 px, subtracao pela constante
lim_adapt = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
cv2.imshow('limiarizacao pela media', lim_adapt)

# GAUSSIANO
# origem, valor maximo, limiarizacao pela media, binarizacao, vizinhanca de 11 px, subtracao pela constante
lim_adapt = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 8)
cv2.imshow('limiarizacao gaussiana', lim_adapt)

cv2.waitKey()
cv2.destroyAllWindows()