import cv2
import pytesseract as pt
from pytesseract import Output

img = cv2.imread("CursoAlura-TextRecognize/Imagens/Aula3-testando.png")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", rgb)

config_tesseract = "--tessdata-dir /home/lanzo/tessdata --psm 6"
result = pt.image_to_data(rgb, config=config_tesseract, lang="por", output_type=Output.DICT)
print(result)

# Slider para o Google Colab
#min_conf = 40 #@param{type: 'slider', min: 0, max: 100}
# Existem outros snippets do Google Colab que podem ser conferidos em: https://cursos.alura.com.br/course/visao-computacional-reconhecimento-texto-ocr-opencv/task/113554

min_conf = 40

# Aula 06 - Bouding Box (caixa delimitadora)

def bounding_box(result, img, color = (255, 100, 0)):
    x = result['left'][i]
    y = result['top'][i]
    w = result['width'][i]
    h = result['height'][i]

    cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)

    return x, y, img

len(result['text'])

# copy_img = rgb.copy()
# for i in range(len(result['text'])):
#     confidence = int(result['conf'][i])
#     if confidence > min_conf:
#         x, y, img = bounding_box(result, copy_img)

# cv2.imshow('copy image', copy_img)

# Aula 07 - Caixa e Texto

copy_img = rgb.copy()
for i in range(len(result['text'])):
    confidence = int(result['conf'][i])
    if confidence > min_conf:
        x, y, img = bounding_box(result, copy_img)
        text = result['text'][i]
        # imagem, posicao do texto, fonte do texto, tamanho do texto, cor do texto
        cv2.putText(copy_img, text, (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
        
cv2.imshow('copy image', copy_img)

# Exercicio

# img = cv2.imread('/content/text-recognize/Imagens/Aula1-teste.png')

# config_tesseract = '--tessdata-dir tessdata'
# resultado = pytesseract.image_to_data(img, config=config_tesseract, lang='por', output_type=Output.DICT)

# img_copia = img.copy()
# for i in range(len(resultado['text'])):
#   confianca = int(resultado['conf'][i])
#   if confianca > min_conf:
#     x, y, img = caixa_texto(resultado, img_copia)

#     texto = resultado['text'][i]
#     cv2.putText(img_copia, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,0,255))

# cv2_imshow(img_copia)


cv2.waitKey()
cv2.destroyAllWindows()
