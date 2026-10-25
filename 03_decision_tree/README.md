# Motor de Análise de Risco Acadêmico - Árvore de Decisão

---

## 1. Objetivo do programa

Esta terceira versão evolui o motor acadêmico para o campo do Aprendizado de Máquina Supervisionado. Em vez de regras lógicas hardcoded, o sistema utiliza um modelo de Árvore de Decisão (`DecisionTreeClassifier`) treinado com um conjunto de dados sintéticos (`dados_alunos.csv`). O modelo aprende de forma automatizada a ponderar múltiplos critérios — incluindo novas variáveis comportamentais e acadêmicas, como a quantidade de trabalhos entregues e o histórico de reprovação prévio — para diagnosticar de forma preditiva o risco do estudante.

---

## 2. Atributos de Avaliação do Modelo

A classificação preditiva considera o vetor de características composto por:
- **Média**: Nota final do aluno (0 a 10).
- **Frequência**: Percentual de presença nas aulas (0 a 100%).
- **Trabalhos Entregues**: Quantidade de entregas realizadas (0 a 5).
- **Histórico de Reprovação**: Indicador binário de reprovações anteriores (0 para nenhum, 1 para histórico existente).

---

## 3. Papel das Classes e Arquivos

O projeto adota uma arquitetura modularizada:
- **aluno.py**: Modela a entidade do estudante com os atributos essenciais (`nome, media, frequencia, trabalhos_entregues, historico_reprovacao`).
- **motor_analise_v3.py**: Gerencia o carregamento do dataset sintético via `pandas`, o treinamento do modelo preditivo com `scikit-learn`, o armazenamento da lista de alunos e o processamento de relatórios estatísticos e consultas.
- **menu.py**: Controla a interface de interação via terminal, validação defensiva de dados numéricos e formatação de telas.
- **main.py**: Ponto de entrada que inicializa o motor, carrega os dados de treino, ajusta o modelo e inicia o loop principal do sistema.

---

## 4. Estrutura de Arquivos

```text
├── data/
│   └── dados_alunos.csv     # Base de dados sintética para treino do modelo
├── aluno.py                 # Definição da classe Aluno
├── motor_analise_v3.py      # Lógica de negócio, carregamento e modelo de IA
├── menu.py                  # Interação via CLI e validações
├── main.py                  # Inicializador do sistema
├── requirements.txt         # Dependências do projeto (pandas e scikit-learn)
└── README.md                # Documentação e instruções de uso
```

---

## 5. Como executar

Com o terminal aberto na raiz do repositório (`python-ai-labs`), siga os passos abaixo:

1. Instale as bibliotecas necessárias para rodar o motor de machine learning utilizando o arquivo de dependências:
    ```bash
    pip install -r 03_decision_tree/requirements.txt
    ```

2. Execute o script principal:
    ```bash
    python 03_decision_tree/main.py
    ```

O programa carregará automaticamente a base de dados de treino, treinará a árvore de decisão e iniciará o menu interativo no terminal.
   