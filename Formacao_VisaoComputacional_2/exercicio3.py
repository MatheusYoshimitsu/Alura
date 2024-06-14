# Exercicio 3 (Aula 15) - Caca-palavras
import cv2
import pytesseract
import os
import re
from matplotlib import pyplot as plt

images_path = 'CursoAlura-TextRecognize/Atividades/Aula 5'
# Para cada arquivo f na lista de os.listdir, o caminho completo eh encontrado usando os.path.join
path = [os.path.join(images_path, f) for f in os.listdir(images_path)]

config_tesseract = '--tessdata-dir /home/lanzo/tessdata'
full_text = ''
txt_name = 'word_search.txt'

# Detecta e printa todos os textos, separando-os por 20 caracteres de '=' + \n
for image in path:
    img = cv2.imread(image)
    image_name = os.path.split(image)[-1] # [-1] indica a ultima posicao
    div_name = '====================\n' + str(image_name)
    full_text = full_text + div_name + '\n'
    text = pytesseract.image_to_string(img, lang = 'por', config = config_tesseract)
    full_text = full_text + text

print(full_text)

# Salvando em txt
txt_file = open(txt_name, 'w+')
txt_file.write(full_text + '\n')
txt_file.close()

# Busca por ocorrencia

search_term = 'ambiente'

# Procura o termo dentro do arquivo escrito
with open(txt_name) as f:
    # findinter encontra o termo de pesquisa dentro do arquivo
    occurrences = [i.start() for i in re.finditer(search_term, f.read())]

print(occurrences) # Localizacao das ocorrencias

# Procura o termo nas imagens
for image in path:
    img = cv2.imread(image)
    image_name = os.path.split(image)[-1]
    print('====================\n' + str(image_name))
    text = pytesseract.image_to_string(img, lang='por', config=config_tesseract)
    occurrences = [i.start() for i in re.finditer(search_term, text)]
    print('Number of occurrences: {}: {}\n'.format(search_term, len(occurrences)))

    cv2.waitKey()
    cv2.destroyAllWindows()