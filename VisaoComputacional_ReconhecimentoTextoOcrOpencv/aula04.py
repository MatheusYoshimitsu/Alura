from PIL import Image
import matplotlib.pyplot as plt
import pytesseract as pt

img = Image.open('CursoAlura-TextRecognize/Imagens/Aula2-livro.png')
plt.imshow(img)
print(pt.image_to_osd(img))

# Exemplo de codigo para rotacionar a imagem
plt.imshow(img.rotate(45))

plt.waitforbuttonpress()