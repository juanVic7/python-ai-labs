# Python AI Labs

**Laboratório de desenvolvimento e experimentação em Inteligência Artificial com Python.**

O `python-ai-labs` reúne projetos que exploram diferentes abordagens de desenvolvimento de sistemas inteligentes, desde a implementação de lógica baseada em regras até modelos de aprendizado de máquina, redes neurais, modelos de linguagem e sistemas de recuperação de conhecimento.

O repositório foi organizado em módulos independentes, cada um dedicado a uma técnica ou arquitetura específica. Essa estrutura permite estudar os fundamentos de cada abordagem, implementar soluções funcionais e comparar como diferentes métodos processam informações, identificam padrões e produzem resultados.

---

## Arquitetura do Projeto

A organização dos módulos acompanha a evolução das técnicas utilizadas ao longo do desenvolvimento, estabelecendo uma base para experimentação, comparação e integração de diferentes componentes de IA.

---

### 01. Fundamentos de Python

`01_python_fundamentals/`

Base de desenvolvimento utilizada nos demais módulos. Reúne exercícios e implementações voltados à organização do código, estruturas de dados, funções, controle de fluxo, manipulação de arquivos, tratamento de exceções e automação com recursos nativos da linguagem.

---

### 02. Inteligência Artificial Simbólica

`02_symbolic_ai/`

Implementação de um sistema de inferência baseado em conhecimento explícito e regras determinísticas. O módulo explora a representação de fatos, a aplicação de condições e a produção de conclusões a partir de critérios previamente definidos.

Essa abordagem permite compreender sistemas cujo processo de decisão pode ser explicado diretamente por suas regras, sem depender do treinamento de modelos estatísticos.

---

### 03. Classificação com Árvores de Decisão

`03_decision_tree/`

Aplicação de aprendizado supervisionado por meio do `DecisionTreeClassifier`, da biblioteca Scikit-Learn. O modelo utiliza atributos estruturados para construir divisões sucessivas no conjunto de dados e classificar registros de acordo com os padrões identificados durante o treinamento.

O módulo utiliza o contexto de risco acadêmico para explorar o treinamento, a predição e a avaliação de um classificador, relacionando os resultados do modelo às características dos dados de entrada.

---

### 04. Classificação com Perceptron

`04_perceptron/`

Estudo de um modelo neural linear utilizado em tarefas de classificação supervisionada. O módulo permite investigar como os pesos são ajustados durante o treinamento, como o modelo estabelece uma fronteira de decisão e quais limitações surgem quando os dados não podem ser adequadamente separados por uma fronteira linear.

Os resultados também servem de referência para comparar o comportamento de diferentes algoritmos sobre o mesmo problema.

---

### 05. Redes Neurais Multicamadas

`05_mlp_classifier/`

Evolução dos experimentos de classificação para uma rede neural multicamadas, implementada com o `MLPClassifier`. O modelo utiliza uma camada oculta, ativação ReLU e normalização dos atributos com `StandardScaler` para aprender relações que não se limitam à separação linear dos dados.

O módulo também explora métricas de avaliação, matriz de confusão e comparação de desempenho, permitindo analisar as diferenças entre modelos com estruturas e capacidades de aprendizado distintas.

---

### 06. Modelos de Linguagem e IA Generativa

`06_llm/`

Integração de um modelo de linguagem executado localmente por meio do Ollama, utilizando o `phi4-mini` para geração de orientações textuais a partir de informações produzidas pelo sistema.

A implementação explora a construção de prompts, a separação entre instruções de sistema e mensagens do usuário e o tratamento de falhas na geração. A arquitetura mantém a análise objetiva do risco acadêmico separada da geração de texto: o motor de análise determina a classificação, enquanto o LLM transforma o resultado em uma orientação contextualizada.

---

### 07. Retrieval-Augmented Generation (RAG)

`07_rag/`

Implementação de uma arquitetura de geração aumentada por recuperação de informações (*Retrieval-Augmented Generation*). O sistema utiliza documentos como fonte de conhecimento, divide o conteúdo em fragmentos contextuais (*chunking*), gera representações vetoriais com o `embeddinggemma` e armazena os vetores no ChromaDB para recuperação posterior.

O módulo também explora a persistência do índice vetorial e o uso de hashes criptográficos para identificar alterações no conteúdo processado. A recuperação de trechos relevantes permite fundamentar a geração de respostas em informações documentais, reduzindo a dependência exclusiva do conhecimento paramétrico do modelo.

---

## Tecnologias e Ferramentas

| Tecnologia | Aplicação no projeto |
|---|---|
| **Python** | Linguagem principal e implementação dos módulos. |
| **Pandas** | Manipulação, preparação e análise de dados tabulares. |
| **Scikit-Learn** | Treinamento, predição e avaliação de modelos de aprendizado de máquina. |
| **Ollama** | Execução local de modelos de linguagem e modelos de embeddings compatíveis. |
| **phi4-mini** | Geração de orientações textuais com um modelo de linguagem local. |
| **embeddinggemma** | Geração de embeddings para representação semântica de conteúdo. |
| **ChromaDB** | Armazenamento persistente e recuperação de vetores. |

---

## Diretrizes de Desenvolvimento

O projeto adota uma organização modular para manter os experimentos isolados e facilitar a evolução de cada implementação.

- **Separação de responsabilidades:** processamento de dados, lógica de análise, inferência e geração textual são tratados como responsabilidades distintas quando aplicável.
- **Experimentação controlada:** os módulos permitem investigar diferentes técnicas de IA aplicadas a problemas relacionados, sem pressupor que um único algoritmo seja adequado a todos os cenários.
- **Avaliação de modelos:** métricas e resultados comparativos são utilizados para examinar o comportamento dos classificadores, considerando suas características e limitações.
- **Execução local:** os experimentos com LLMs e embeddings utilizam modelos executados pelo Ollama, sem depender necessariamente de serviços externos de inferência.
- **Evolução incremental:** cada módulo amplia o escopo técnico do repositório e estabelece uma base para experimentos posteriores.

---

## Objetivo

Construir um conjunto de implementações que permita compreender, desenvolver e avaliar diferentes arquiteturas de Inteligência Artificial, explorando desde mecanismos explícitos de decisão até sistemas capazes de aprender padrões e recuperar conhecimento para gerar respostas contextualizadas.

O `python-ai-labs` funciona como um ambiente contínuo de estudo, experimentação e desenvolvimento, no qual cada módulo contribui para a construção de uma visão mais ampla sobre o funcionamento e a aplicação prática de sistemas inteligentes.