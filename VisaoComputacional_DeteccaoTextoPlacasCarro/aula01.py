# Aula 1: Comecando identificacao de texto em imagens
import cv2
import pytesseract as pt
#from google.colab.patches import cv2_imshow

image1 = cv2.imread('imagens/trecho_livro.png')

#cv2_imshow(image)
cv2.imshow('Image 1',image1)

# indica o diretorio da configuracao e o modo desejado
config = '--tessdata-dir /home/lanzo/tessdata --psm 6'
lang = 'por'

text = pt.image_to_string(image1, lang, config)
print(text)

cv2.waitKey(0)
cv2.destroyAllWindows()