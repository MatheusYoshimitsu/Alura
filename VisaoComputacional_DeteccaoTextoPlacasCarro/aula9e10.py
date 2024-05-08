# Aula 9 e 10 - Bordas e Contornos
import cv2

# Import
image = cv2.imread('/mnt/c/Users/matheus.lanzo/OneDrive - Usebens Seguradora S A/Área de Trabalho/Alura/VisaoComputacional_DeteccaoTextoPlacasCarro/imagens/placa_carro1.png')
# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Otsu
valor, lim_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Deteccao de bordas de Canny
bordas0 = cv2.Canny(gray, 100, 200) # 100 e 200 vieram do exemplo da documentacao
cv2.imshow('Canny Image 0', bordas0)

# Desafio
bordas1 = cv2.Canny(gray, 0, 100)
cv2.imshow('Canny Image 1', bordas1)

bordas2 = cv2.Canny(gray, 200, 600)
cv2.imshow('Canny Image 2', bordas2)

bordas3 = cv2.Canny(gray, 16, 240)
cv2.imshow('Canny Image 3', bordas3)

# Contorno
# imagem, hierarquia, coordenadas de cada um dos pixels
contornos, hierarquia = cv2.findContours(bordas0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contornos)

cv2.waitKey()
cv2.destroyAllWindows()