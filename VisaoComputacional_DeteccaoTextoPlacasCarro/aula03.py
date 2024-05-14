# Aula 3: Limiarizacao simples
import cv2

imagem = cv2.imread('imagens/placa_carro1.png')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # converte a imagem para cinza

# Teste 0
limiar = 30
valor, lim_simples = cv2.threshold(imagem, limiar, 255, cv2.THRESH_BINARY)
cv2.imshow('Imagem 0', lim_simples)

# Teste 1
limiar = 127
valor, lim_simples = cv2.threshold(imagem, limiar, 255, cv2.THRESH_BINARY)
cv2.imshow('Imagem 1', lim_simples)

# Teste 2
limiar = 180
valor, lim_simples = cv2.threshold(imagem, limiar, 255, cv2.THRESH_BINARY)
cv2.imshow('Imagem 2', lim_simples)

# o método threshold devolve 2 resultados, o valor do limiar e a imagem limiarizada

print(valor);

cv2.waitKey();
cv2.destroyAllWindows();