# Motor de Análise de Risco Acadêmico - Deep Learning (MLPClassifier)

---

## 1. Objetivo

Esta etapa evolui o motor de análise acadêmica para o campo do Deep Learning e das redes neurais artificiais multicamadas. Em vez de árvores de decisão ou modelos lineares simples, o sistema utiliza o "MLPClassifier" (Multi-Layer Perceptron) do Scikit-Learn, integrado ao processo de padronização de dados com "StandardScaler", para aprender padrões complexos e não lineares a partir do dataset sintético (`dados_alunos.csv`).

O objetivo é aplicar uma rede neural artificial à classificação do risco acadêmico, explorando a capacidade desse tipo de modelo de identificar relações entre diferentes características dos alunos.

---


## 2. Arquitetura da Rede Neural

A arquitetura configurada no script utiliza o `MLPClassifier`, que implementa um perceptron multicamadas. O modelo possui uma camada oculta com cinco neurônios, responsáveis por aprender representações intermediárias dos dados durante o treinamento.

Os principais parâmetros utilizados são:
- `hidden_layer_sizes=(5,)`: define uma camada oculta com cinco neurônios.
- `activation="relu"`: utiliza a função de ativação ReLU, que permite representar relações não lineares.
- `max_iter=2000`: estabelece um limite de até 2.000 iterações para o processo de treinamento.
- `StandardScaler`: padroniza as características numéricas antes de serem utilizadas pela rede neural.

A combinação desses componentes permite que o modelo aprenda relações mais complexas entre as variáveis de entrada, diferentemente de abordagens lineares mais simples.

---

## 3. Como executar o programa

Para executar o programa, abra o terminal na raiz do repositório (`python-ai-labs`) e siga os passos abaixo.

1. Primeiro, instale as dependências do projeto:
   ```bash
   pip install -r 05_mlp_classifier/requirements.txt
   ```

2. Em seguida, execute o script principal:
   ```bash
   python 05_mlp_classifier/motor_analise_v4.py
   ```

O programa carregará automaticamente a base de dados, realizará o treinamento da rede neural multicamada e iniciará o menu interativo no terminal, permitindo utilizar as funcionalidades de análise de risco acadêmico.

---

## 5. Resultados dos testes

Nos testes de desempenho realizados em um conjunto de teste isolado, correspondente a 20% da base de dados, o modelo atingiu uma acurácia de 96,7%. A comparação de desempenho indicou que o `MLPClassifier` obteve esse resultado, demonstrando sua capacidade de identificar relações não lineares entre as características dos alunos por meio da camada oculta e da função de ativação ReLU.

A matriz de confusão gerada pelo modelo foi:
```text
[[170   0   4]
 [  0  15   1]
 [  2   1  47]]
```

Essa matriz permite analisar a distribuição das classificações corretas e dos erros entre as três classes avaliadas pelo modelo. Os valores da diagonal principal representam as previsões corretas, enquanto os demais valores indicam as classificações incorretas.

## 6. Conclusão

A transição para redes neurais multicamadas, introduzindo conceitos fundamentais de Deep Learning, proporcionou resultados expressivos na análise de risco acadêmico. A acurácia de 96,7% demonstra o potencial do `MLPClassifier` para identificar padrões nos dados utilizados, superando as limitações de modelos mais simples nesse experimento.

O projeto também evidencia a importância do pré-processamento dos dados por meio do `StandardScaler`, especialmente para o treinamento de redes neurais, e da configuração adequada da arquitetura da rede. Esses elementos contribuem para o desenvolvimento de um modelo capaz de realizar previsões com alto desempenho na base de dados utilizada, mantendo a possibilidade de futuras melhorias na arquitetura, na validação e na generalização dos resultados.