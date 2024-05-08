# Aula 6 - Erosão e Dilatação

### Kernel
Máscara formada por uma matriz de valores, podendo ser esta de diversas formas, commo retangular, elíptica ou até mesmo em cruz.  
É possível atribuir diferentes valores para o kernel, sendo possível fazer outras operações com os pixels da imagem, algo chamado de **convolução**, retornando uma figura transformada.

## Erosão:
Diminui a área branca da imagem.  
Útil para remover ruídos brancos pequenos, separar dois objetos conectados, etc.  
Considera que caso ao menos um pixel da vizinhança não seja branco, transforma o pixel em si em preto. 

## Dilatação
Expande a área branca da imagem.
Oposto da erosão. Considera que caso ao menos um pixel da vizinhança não seja preto, transforma o pixel em si em branco. 

# Aula 7 - Abertura e Fechamento
A espessura da imagem original é mantida nos dois casos.

## Abertura
Erosão seguida de dilatação.  
Serve para retirar ruídos do lado de fora do contorno branco.

## Fechamento
Dilatação seguida de erosão.  
Serve para retirar ruídos do lado de dentro do contorno branco.

# Aula 8 - Outras transformações

## Gradiente morfológico

Diferença entre dilatação e erosão de uma imagem. O resultado será algo como o contorno do objeto.

## Cartola (Top Hat)

Diferença entre a imagem original e a abertura da imagem. Auxilia detecção de partes claras em fundos escuros.

## Chapéu Preto (Black Hat)

Diferença entre o fechamento e da imagem de entrada. Auxilia na detecção de partes escuras em fundos claros.

**1. ABERTURA:** Reduzir ruídos brancos na imagem sem alterar a espessura original dos objetos  
**2. FECHAMENTO:** Reduzir ruídos pretos na imagem sem alterar a espessura original dos objetos  
**3. GRADIENTE:** Manter o contorno do objeto  
**4. TOP HAT:** Destacar regiões claras em fundos escuros  
**5. BLACK HAT:** Destacar regiões escuras em fundos claros  

# Aula 9

## Detecção de borda de Canny
1. Retirar ruídos
2. Encontrar a intensidade de gradiente usando Sobel
3. Retirar ruídos que não pertençam à borda. O resultado será uma imagem binária com bordas finas
4. Novos limiares para encontrar as bordas verdadeiras e falsas. 
* Bordas fora dos limiares, mas que estejam conectadas com bordas dentro dos limiares, são consideradas como verdadeiras. Da mesma forma, bordas dentro destes limiares, mas sem conexões, são consideradas como falsas e, portanto, descartadas.
* Nesta etapa, ruídos pequenos também serão removidos. O resultado seriam bordas grossas na imagem.