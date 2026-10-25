# Motor de Análise de Risco Acadêmico - Comparação de Modelos de Machine Learning

---

## 1. Objetivo

Esta etapa evolui o motor acadêmico para uma fase de experimentação e avaliação comparativa entre diferentes algoritmos de aprendizado de máquina supervisionado. O programa carrega um conjunto de dados sintéticos (`dados_alunos.csv`), realiza a divisão estratificada em bases de treino e teste, e treina múltiplos modelos para classificar o risco acadêmico, analisando quantitativamente qual abordagem se ajusta melhor à lógica do problema.

---

## 2. Modelos Avaliados e Justificativa

O script compara o comportamento de abordagens distintas frente aos indicadores acadêmicos (`media` e `frequencia`):

- **Árvore de Decisão** (`DecisionTreeClassifier`): Selecionada como modelo principal. É ideal para este problema porque as regras de risco acadêmico dependem de limiares e divisões ortogonais bem definidas ("E" / "OU"). A árvore particiona o espaço de características de forma natural, sendo altamente intuitiva e imune à diferença de escala entre a média (0 a 10) e a frequência (0 a 100%).
- **Perceptron**: Modelo linear de classificação que opera em conjunto com a normalização de dados (`StandardScaler`). Foi incluído para testar a capacidade de separação linear das fronteiras de risco acadêmico.
- 
---

## 3. Papel dos Componentes do Código

O projeto mantém a modularidade dentro da estrutura adotada:
- **comparacao_modelos.py**: Contém a classe MotorAnalise, responsável pelo carregamento dos dados via pandas, divisão de treino e teste, treinamento simultâneo das arquiteturas do Scikit-Learn, extração de acurácia, geração de matrizes de confusão e execução das previsões (tanto os testes automatizados quanto a interação com o usuário via terminal).
- **Dataset (`data/dados_alunos.csv`)**: Base sintética com 70 registros utilizada para o treinamento e validação dos modelos.

---

## 4. Como Executar

Com o terminal aberto na raiz do repositório (`python-ai-labs`), siga os passos abaixo:
1. Instale as bibliotecas necessárias para rodar o pipeline de machine learning:
   ```bash
   pip install -r 04_perceptron/requirements.txt
   ```
2. Execute o script de comparação de modelos:
   ```bash
   python 04_perceptron/comparacao_modelos.py
   ```
O programa exibirá no terminal o carregamento da base, os resultados comparativos de acurácia e matrizes de confusão, os testes automáticos de previsão e o menu interativo para novos diagnósticos.

---

## 5. Resultados Obtidos e Desempenho

Os modelos foram avaliados em um conjunto de teste isolado (20% da base):

### 5.1 Tabela Comparativa de Desempenho

| Modelo | Acurácia no Teste | Desempenho Geral |
|---|---|---|
| Árvore de Decisão | 92.9% | Excelente desempenho. Conseguiu mapear com precisão os limites das faixas de notas e frequências, errando apenas 1 amostra de risco moderado. |
| Perceptron | 50.0% | Desempenho limitado. Por ser um classificador linear simples, encontrou dificuldades com a não-linearidade das fronteiras de decisão dos riscos acadêmicos. |

### 5.2 Matrizes de Confusão

**Árvore de Decisão:**
```text
[[5 0 0]
 [0 5 0]
 [1 0 3]]
```

**Perceptron:**
```text
[[3 0 2]
 [0 0 5]
 [0 0 4]]
```

---

## 6. Conclusão dos Testes

A Árvore de Decisão demonstrou ser amplamente superior e ideal para este cenário. Como as regras acadêmicas de risco se baseiam em cortes específicos e condicionais (como média inferior a 6 e frequência menor que 75%), a estrutura de árvore se alinha perfeitamente à lógica do problema, garantindo alta precisão preditiva e atendendo com robustez ao propósito do desenvolvimento.