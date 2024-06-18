# Curso Alura: Redes Neurais: Deep Learning com PyTorch

## História das Redes Neurais

1943: primeiro modelo neural

* Dendritos
* Corpo
* Axônios

1957: Perceptron. Associando um peso a cada neurônio.

* **Perceptrons só funcionam em funções lineares!**

1986: Multi-Layer Perceptron e Backpropagation. Permite o aprendizado de funções mais complexas

### Teorema da Aproximação Universal

Uma rede neural com uma única camada escondida é suficiente para representar qualquer função.

2006: Deep Learning. Hardware mais robutos e abundância de dados permitiram o avanço das redes neurais.

[Ferramentas interessantes](https://cursos.alura.com.br/course/pln-deep-learning/task/66804)

* Classificação de Imagens
* Transferência de estilo: filtro de Instagram
* Modelo de Linguagem: ChatGPT

## Aula prática 01 - Tensores

São arrays de N dimensões. Um número isolado é considerado um tensor 0D.

* Esta aula será feita em um notebook Jupyter para facilitar a visualização dos tipos de dados

## Aula prática 02 - Classificação Linear

Classificadores lineares são nada mais do que retas. Se os pontos estiverem acima da reta, os serão positivos. Se estiverem abaixo, negativos. Ou seja, uma simples reta funciona como classificador.

$$ax + by + c$$

se transforma em:

$$w_1x_1 + w_2x_2 + b$$

onde $w_n$ é o peso (*weight*), $x_n$ é a característica de entrada (*input feature*) e $b$ é o viés (*bias*).

De forma genérica, a função de mapeamento de um modelo linear é:

$$ y = \sum_{i=1}^{d} w_ix_i + b$$
