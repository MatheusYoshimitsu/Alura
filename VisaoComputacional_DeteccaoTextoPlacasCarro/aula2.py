# Aula 2: Tentativa de identificacao de outra imagem
import cv2
import pytesseract as pt
#tesseract --help-psm

image1 = cv2.imread('/mnt/c/Users/matheus.lanzo/OneDrive - Usebens Seguradora S A/Área de Trabalho/Alura/VisaoComputacional_DeteccaoTextoPlacasCarro/imagens/placa_carro1.png')

# indica o diretorio da configuracao e o modo desejado
config = '--tessdata-dir /home/lanzo/tessdata --psm 6'
lang = 'por'

image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image 1', image1)
text = pt.image_to_string(image1, lang, config)
print(text)

# O tesseract nao conseguiu identificar de forma satisfatoria
# portanto, é necessario passar por um pre-processamento

cv2.waitKey(0)
cv2.destroyAllWindows()