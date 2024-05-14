import cv2
import pytesseract as pt
from pytesseract import Output

img = cv2.imread("CursoAlura-TextRecognize/Imagens/Aula3-testando.png")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", rgb)

config_tesseract = "--tessdata-dir /home/lanzo/tessdata --psm 6"
resultado = pt.image_to_data(rgb, config=config_tesseract, lang="por", output_type=Output.DICT)
print(resultado)

# Slider para o Google Colab
#min_conf = 40 #@param{type: 'slider', min: 0, max: 100}
# Existem outros snippets do Google Colab que podem ser conferidos em: https://cursos.alura.com.br/course/visao-computacional-reconhecimento-texto-ocr-opencv/task/113554

min_conf = 40

# Aula 07 - Bouding Box (caixa delimitadora)

def caixa_texto(resultado, img, cor = (255, 100, 0)):
    x = resultado['left'][i]
    y = resultado['top'][i]
    w = resultado['width'][i]
    h = resultado['height'][i]
    return

# Finalizar aula

cv2.waitKey()
cv2.destroyAllWindows()
