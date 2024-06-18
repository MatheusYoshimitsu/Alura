# Treinando uma Rede Neural: Deep Learning com PyTorch

## Cross-Entropy

Minimzar a entropia das distribuições

## Gradiente (de forma simples)

Indicador se o "passo" melhorou ou piorou o modelo, com base em uma medida de qualidade (loss)

## Otimização

Uso do gradiente para escolher a próximo passo

## Estruturas padrão

Por enquanto, precisamos de 3 principais elementos: as classes a serem analisadas, o dados das features dessas classes e o target.

> Processos como a padronização e a normalização levam todos os dados para uma escala similar, enquanto mantêm as suas distribuições originais

## Forward e Backpropagation

* Definições vistas de forma melhor nos vídeos, mas as aplicações práticas se resumem a aplicar uma função (forward) e ajustá-la na próxima iteração (backpropagation).

## Bacth

Quantidade de amostras em uma iteração. Seu tamanho influencia diretamente o comportamento da convergência.

* Batch estocástico: uma única amostra
* Mini-batch: subconjunto do treino
* Batch: conjunto do treino completo

## Época

Quanto todas as amostras do conjunto de treino foram vistas pelo modelo.

Posso dizer então que uma época é na verdade, uma iteração de todas as iterações?

```py
# Epochs
for i in range(num_epochs):

    # Iterations
    for batch in train_data:

        # Forward
        ypred = net(batch)
        loss = criterion(ypred, y)
        
        # Backpropagation
        loss.backward()
        optimizer.step()
```

## DataLoader

É um dos destaques do PyTorch. Tem um ótimo gerenciamento de carregamentos de dados para o treinamento de RNs:

* Separação dos dados em batches
* Embaralhamento dos dados
* Carrega batches em paralelo usando threads

## Métricas de qualidade

Como o projeto final se deu por uma reta de regressão linear, não é possível usar medidas como acurácia para saber o quão bom o modelo está. No entanto, podemos usar outros tipos de métricas, como por exemplo, analisando as distâncias dos pontos e linha.

### Importante

* Conferir os notebooks da aula, eles têm mais informações descritas além do código feito em aula. Podem ajudar a complementar os comentários dos exercícios feitos

* Na dúvida, usa o Adam $\rightarrow$ um dos melhores otimizadores adaptativos

* Devido à lentidão de performance entre CPU vs GPU, o projeto final será feito no Google Colab
