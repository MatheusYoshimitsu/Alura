# Aula 01 - OCR no Colab
import cv2
import pytesseract as pt

test_img = cv2.imread('CursoAlura-TextRecognize/Imagens/Aula1-teste.png')
cv2.imshow('teste', test_img)
text = pt.image_to_string(test_img)
print(text)

# Aula 02 - Imagens BGR
ocr_img = cv2.imread('CursoAlura-TextRecognize/Imagens/Aula1-ocr.png')
cv2.imshow('tesseract ocr', ocr_img)
text = pt.image_to_string(ocr_img)
print(text)

rgb = cv2.cvtColor(ocr_img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)
text = pt.image_to_string(rgb)
print(text)

grayscale = cv2.cvtColor(ocr_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', grayscale)
text = pt.image_to_string(grayscale)
print(text)

cv2.waitKey()
cv2.destroyAllWindows()