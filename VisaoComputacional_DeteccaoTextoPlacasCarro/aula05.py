# Aula 5: Limiarizacao de Otsu
import cv2
import seaborn as sns
import matplotlib.pyplot as plt
import pytesseract as pt

# Importa a imagem
image = cv2.imread('imagens/placa_carro1.png')
# RGB para cinza
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Podemos ver a imagem como um array
print(image);

# Podemos tambem plotar esse grafico
# flatten transforma nosso multi-D array para 1D array
ax = sns.histplot(image.flatten())
ax.figure.set_size_inches(10,6)

# origem, valor limiar, valor caso seja maior que o limiar, binarizado e otsu
valor, lim_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('limiarizacao de otsu', lim_otsu)
print(f'Limiar: {valor}')

config = '--tessdata-dir /home/lanzo/tessdata --psm 6'
text = pt.image_to_string(lim_otsu, 'por', config)
print(text);

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()