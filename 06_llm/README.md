# Motor de Análise de Risco Acadêmico - IA Generativa e LLMs (Ollama)

---

## 1. Objetivo

Esta etapa evolui o ecossistema do projeto ao integrar a Inteligência Artificial Generativa como camada final de comunicação institucional. Enquanto as etapas anteriores focavam estritamente na tomada de decisão preditiva (através de regras, árvores de decisão, redes neurais e classificadores MLP), esta versão transforma dados numéricos estruturados em orientações textuais humanizadas, acolhedoras e contextualizadas para o estudante.

---

## 2. Arquitetura e Componentes do Código

Diferente das versões anteriores baseadas em classificadores preditivos, este módulo implementa uma arquitetura voltada exclusivamente para a geração de linguagem natural:

1. Estrutura de Dados Fictícios (`DADOS_FICTICIOS`): Uma lista de dicionários contendo os atributos dos estudantes (`nome, media, frequencia e situacao_informada`), simulando o cenário de entrada para a geração dos textos.  
2. Classe `GeradorOrientacaoAcademica`: Responsável por centralizar a lógica de interação com a IA:
    - `gerar_prompt`: Constrói dinamicamente a instrução textual contendo os dados do aluno e um conjunto rígido de regras e restrições institucionais.  
    - `gerar_orientacao`: Realiza a chamada à API local do Ollama separando o contexto em papéis (system para o comportamento institucional e user para a tarefa específica), aplicando parâmetros como `temperature=0.3` para maior objetividade.  
    - `validar_mensagem e mensagem_fallback`: Garantem a resiliência do sistema, validando o tamanho da resposta ou acionando uma mensagem alternativa caso ocorra alguma falha na execução do modelo local.

---

## 3. Servidor e Modelo Utilizados

- Servidor de Inferência: `Ollama` (execução local em ambiente isolado via API REST local).
- Modelo de Linguagem: `phi4-mini`.  

---

## 4. Instrucoes de Instalacao e Execucao

1. Certifique-se de que o servico do Ollama esta instalado e em execucao no seu computador.
2. Baixe o modelo utilizado no terminal com o comando:
   ```bash
   ollama pull phi4-mini
   ```
3. Instale a biblioteca Python necessaria listada no projeto:
   ```bash
   pip install -r 06_llm/requirements.txt
   ```
4. Execute o programa principal:
   ```bash
   python 06_llm/gerar_orientacao_academica.py
   ```

---

## 5. Comentario Final
   
Durante o desenvolvimento, foi possivel compreender como estruturar prompts eficientes utilizando o isolamento de papeis (sistema e usuario) para guiar o comportamento de modelos de linguagem locais. Uma dificuldade observada foi a tendencia ocasional de os LLMs introduzirem recomendacoes padronizadas (genericas) mesmo quando o cenario do aluno e totalmente positivo, o que reitera a importancia de uma validacao adequada e de restricoes claras no prompt.
