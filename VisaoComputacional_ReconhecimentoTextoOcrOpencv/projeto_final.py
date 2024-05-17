# Aula 13 - Preparando o ambiente (projeto final)
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pytesseract as pt
from pytesseract import Output
from PIL import Image, ImageFont, ImageDraw
import os
import re

project = 'CursoAlura-TextRecognize/Imagens/Projeto'
# Para cada arquivo f na lista de os.listdir, o caminho completo eh encontrado usando os.path.join
path = [os.path.join(project, f) for f in os.listdir(project)] # caminho de todas as imagens
# print(path)

def show_images(img):
    fig = plt.gcf() # busca a figura atual
    fig.set_size_inches(10,5)
    plt.axis('off') # remove a visualizacao de eixos
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # conversao de cores com OpenCV
    plt.show() # mostra a imagem

for image in path:
    image = cv2.imread(image)
    # show_images(image)

config_tesseract = '--tessdata-dir /home/lanzo/tessdata'

# def ocr_process(img, config_tesseract):
#     text = pt.image_to_string(img, lang='por', config=config_tesseract)
#     return text

# Imagens utilizadas de: https://cursos.alura.com.br/course/visao-computacional-reconhecimento-texto-ocr-opencv/task/113566

# Aula 14 - Reconhecimento de texto

full_text = ''
txt_name = 'ocr_results.txt'

for image in path:
    img = cv2.imread(image)
    image_name = os.path.split(image)[-1] # nomes e diretórios quebrados das imagens. [-1] indica a ultima posicao
    div_name = '====================\n' + str(image_name) # divisao + nome da imagem atual
    full_text = full_text + div_name + '\n'
    text = pt.image_to_string(img, lang='por', config=config_tesseract)
    full_text = full_text + text

print(full_text)

# Salvando em txt
txt_file = open(txt_name, 'w+') # w+ escreve no arquivo /// a+ escreve no final do arquivo
txt_file.write(full_text + '\n')
txt_file.close()

# Aula 15 - Busca por ocorrencia

search_term = 'learning'

# Procura o termo dentro do arquivo escrito
with open(txt_name) as f:
    # findinter encontra o termo de pesquisa dentro do arquivo
    occurrences = [i.start() for i in re.finditer(search_term, f.read())] # Ocorrencia eh uma lista
print(occurrences)

# Procura o termo nas imagens
for image in path:
    img = cv2.imread(image)
    image_name = os.path.split(image)[-1]
    print('====================\n' + str(image_name))
    text = pt.image_to_string(img, lang='por', config=config_tesseract)
    occurrences = [i.start() for i in re.finditer(search_term, text)] # Ocorrencia eh uma lista
    print('Number of occurrences: {}: {}\n'.format(search_term, len(occurrences)))

# Aula 16 - Reconhecimento na imagem

font_dir = 'CursoAlura-TextRecognize/Imagens/calibri.ttf'
min_conf = 30

def bounding_box(i, result, img, color = (255, 100, 0)):
    x = result['left'][i]
    y = result['top'][i]
    w = result['width'][i]
    h = result['height'][i]

    cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)

    return x, y, img

def write_text(text, x, y, img, font_dir, color = (50,50,255),text_size = 16):
    font = ImageFont.truetype(font_dir, text_size)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x, y - text_size), text, font = font, fill = color)
    img = np.array(img_pil)
    return img

def ocr_process_image(img, search_term, config_tesseract, min_conf):
    result = pt.image_to_data (img, config=config_tesseract, lang='por', output_type=Output.DICT) # imagem para dados
    num_occurrences = 0
    
    for i in range(0, len(result['text'])): # 0 ao numero de vezes que aparece text
        confidence = int(result['conf'][i])
        if confidence > min_conf:
            text = result['text'][i]
            # # solucao do desafio pela aula
            # if search_term.lower() in texto.lower(): 
            # (...)
            if re.match(search_term, text):
                x, y, img = bounding_box(i, result, img, (0,0,255))
                img = write_text(text, x, y, img, font_dir, (50,50,255), 14)
                num_occurrences += 1

    return img, num_occurrences

search_term = '[Ll][Ee][Aa][Rr][Nn][Ii][Nn][Gg]' # encotrar maiusculas e minusculas

for image in path:
    img = cv2.imread(image)
    original_img = img.copy()
    image_name = os.path.split(image)[-1]
    print('====================\n' + str(image_name))
    img, num_occurrences = ocr_process_image(img, search_term, config_tesseract, min_conf)
    print('Number of occurrences for {} in {}: {}\n'.format(search_term, image_name, num_occurrences))
    show_images(img)

# Salvando todas as imagens

for image in path:
    img = cv2.imread(image)
    original_img = img.copy()
    image_name = os.path.split(image)[-1]
    img, num_occurrences = ocr_process_image(img, search_term, config_tesseract, min_conf)
    if num_occurrences > 0:
        show_images(img)
        new_image_name = 'OCR_' + image_name
        new_image = 'images_tesseract/' + str(new_image_name)
        cv2.imwrite(new_image, img)

cv2.waitKey()
cv2.destroyAllWindows()