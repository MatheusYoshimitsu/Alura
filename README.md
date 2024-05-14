# Cursos Alura

Neste repositório, estarei colocando meus materiais de estudo dos cursos Alura.

## Para os cursos de Visão Computacional (Python) foram necessários instalar

### Tesseract

Simples de instalar usando APT. Pode-se usar o seguinte comando:

```bash
sudo apt install tesseract-ocr
```

Deve-se instalar também os idiomas de OSD e Português.  
Podem ser facilmente encontrados em: <https://github.com/tesseract-ocr/tessdata>  
Exemplo de instalação de idioma usando Linux:  

1. Criar diretório para instalação:  

```bash
mkdir tessdata  
```

2. Baixar arquivo, nomeá-lo e inserí-lo no diretório (este é o único passo que deve ser repetido para cada novo idioma):

```bash
wget -O ./tessdata/por.traineddata https://github.com/tesseract-ocr/tessdata/raw/main/por.traineddata
```

3. Atualizar o PATH em bashrc.

```bash
nano ~/.bashrc
```

4. Inserir a seguinte linha no final do arquivo:

```bash
export TESSDATA_PREFIX="/home/NOME_USUARIO/tessdata"
```

Caso a biblioteca matplotlib ainda não esteja instalada:

```bash
pip install matplotlib
```

Pode ser necessário instalar backends que suportem as funções para plotar as imagens usando GUI da biblioteca matplotlib.  
Algumas sugestões possíveis (se uma funcionar, não é necessário instalar outra):

* GTK3Agg
  
```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

* QtAgg ou Qt5Agg
  
```bash
sudo apt install python3-pyqt5
```

### OpenCV, NumPy, PyTesseract e Scikit

Simples de instalar usando PIP. Pode-se usar os seguintes comandos:

```bash
pip install opencv-python
pip install numpy
pip install pytesseract
pip install scikit-image
```
