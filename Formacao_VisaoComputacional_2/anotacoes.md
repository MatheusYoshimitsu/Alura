# Anotações do Curso de Reconhecimento de Texto com OCR e OpenCV

## Aula 01

### Etapas

* Aquisição da imagem (imagem de entrada)
* Pré-processamento
* Reconhecimento com o Tesseract OCR (2 opções)
  * Reconhecimento de padrões
    * Exemplos de texto em várias fontes
  * Detecção de recursos
    * Algo mais "bruto". Talvez essa abordagem seja útil para reconhecimento de chassis
* Pós-processamento
* Resultado final

### Biblioteca Leptonica

Útil para processamento e análise de imagens. É usada no Tesseract

## Aulas 02, 03 e 04

Estas aulas explicam melhor os diferentes idiomas e Page Segmentation Modes (PSM's) do Tesseract, algo já visto no curso anterior de Visão Computacional.  
É possível listar os idiomas com o comando:

```bash
tesseract --list-langs
```

E também é possível listar os PSM's com o comando:

``` bash
tesseract --help-psm
```

As particularidades de cada PSM pode ser visto no material do curso em <https://cursos.alura.com.br/course/visao-computacional-reconhecimento-texto-ocr-opencv/task/113548>  
Destacam-se alguns modos interessantes:  

* "**PSM 4 - Assuma uma única coluna de texto de tamanhos variáveis:** O OCR nesse caso lê a imagem como uma coluna, linha a linha, mesmo com textos de diferentes tamanhos. Isso pode ser aplicado por exemplo em dados de planilhas, tabelas ou recibos"
* "**PSM 6 - Assuma um único bloco uniforme de texto:** Esse modo de segmentação pode ser utilizado para textos como páginas de livros, por exemplo, que tem uma única fonte. Nesses casos, quando o texto é uma única fonte sem qualquer variação, temos um texto uniforme e simples para o Tesseract compreender."
* "**PSM 7 - Trate a imagem como uma única linha de texto:** Esse modo é utilizado quando trabalhamos com uma única linha de texto uniforme, como por exemplo placas de carro."

## Aula 05

### Orientation and Script Detection (OSD)

Seu retorno são os metadados da imagem.

---

## Comandos úteis para downloads

Criar diretório para instalação:

```bash
mkdir NOME_DIR  
```

Exemplo:

```bash
mkdir tessdata  
```

Baixar arquivo, nomeá-lo e inserí-lo no diretório:

```bash
wget -O CAMINHO_DIR/NOME_ARQUIVO LINK_DOWNLOAD
```

Exemplo:

```bash  
wget -O ./tessdata/osd.traineddata https://github.com/tesseract-ocr/tessdata/raw/main/osd.traineddata
```

## Aula 11 - Cenários Naturais

### Métricas de Avaliação

![Metricas de Avaliacao](https://www.researchgate.net/publication/336402347/figure/fig3/AS:812472659349505@1570719985505/Calculation-of-Precision-Recall-and-Accuracy-in-the-confusion-matrix.ppm)

* Verdadeiros positivos, verdadeiros negativos, falsos positivos e falsos negativos
* Acurácia: proporção de acertos em relação a todas as previsões realizadas.
* Precisão: proporção de VP por VP e FP
* Sensibilidade: proporção de VP por VP e FN

* *Taxa de Verdadeiros Positivos e Taxa de Verdadeiros Negativos podem ser calculadas usando matriz de confusão*

## Aula Extra - Curva ROC (Receiving Operating Characteristic Curve)

Também chamada de Curva Característica de Operação do Receptor, serve para avaliar modelos de classificação binária.

* **Area Under the Curve (AUC):** quanto mais perto de 1, melhor o desempenho de classificação

O ponto de corte é de extrema importância para o classificador.

Para mais detalhes: <https://cursos.alura.com.br/extra/alura-mais/curva-roc-c1465>

## Finalização do curso

Há outros OCRs disponíveis, entre eles, o Keras OCR e Easy OCR. Em uma aula do Alura+, é possível conferir um pouco sobre o Easy OCR, que tem suporte a mais de 80 idiomas e pode produzir resultados sem pré-processamento, mais interessantes que o Tesseract.
