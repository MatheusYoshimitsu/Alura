# Cursos Alura
Neste repositório, estarei colocando meus materiais de estudo dos cursos Alura.

## Para os cursos de Visão Computacional (Python) foram necessários instalar:

### Tesseract

Simples de instalar usando APT. Pode-se usar o seguinte comando:
```
sudo apt install tesseract-ocr
```

Deve-se instalar também os idiomas de OSD e Português.  
Podem ser facilmente encontrados em: https://github.com/tesseract-ocr/tessdata  
Exemplo de instalação de idioma usando Linux:  
1. Criar diretório para instalação:  
```
mkdir tessdata  
```
2. Baixar arquivo, nomeá-lo e inserí-lo no diretório (este é o único passo que deve ser repetido para cada novo idioma):
```  
wget -O ./tessdata/osd.traineddata https://github.com/tesseract-ocr/tessdata/raw/main/osd.traineddata
```
3. Atualizar o PATH em .bashrc.
```
nano ~/.bashrc
```
3. Inserir a seguinte linha no final do arquivo:
```
export TESSDATA_PREFIX="/home/NOME_USUARIO/tessdata"
```

* Pode ser necessário instalar backends que suportem as funções para plotar as imagens usando GUI da biblioteca matplotlib.  
Algumas sugestões possíveis (se uma funcionar, não é necessário instalar outra):
    *  GTK3Agg
    * QtAgg 
    * Qt5Agg

### OpenCV, NumPy e PyTesseract

Simples de instalar usando PIP. Pode-se usar os seguintes comandos:

```
pip install opencv-python
pip install numpy
pip install pytesseract
```