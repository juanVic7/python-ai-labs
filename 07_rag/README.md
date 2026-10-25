# Motor de Análise de Risco Acadêmico — Aplicação RAG Vetorial (ChromaDB e Ollama)

---

## 1. Objetivo

Esta etapa evolui o projeto para o universo de `Retrieval-Augmented Generation` (RAG) com busca vetorial local. O objetivo principal é capacitar a aplicação a consultar de forma inteligente uma base documental própria (regulamentos acadêmicos) antes de responder a uma pergunta. Em vez de depender exclusivamente do conhecimento estático do modelo de linguagem, o sistema recupera trechos contextualmente relevantes utilizando embeddings e fornece essa base de dados estrito para que o LLM formule respostas precisas, respaldadas pelas fontes e livres de alucinações.

---

## 2. Explicação da Aplicação e Funcionamento

A aplicação foi desenhada para operar localmente, garantindo privacidade, autonomia e rastreabilidade através da integração entre Python, ChromaDB e Ollama. O fluxo de funcionamento divide-se nas seguintes etapas lógicas: 
1. **Carregamento e Particionamento (`Chunking`)**: Os documentos institucionais em formato Markdown localizados na pasta `documentos` são lidos e divididos em blocos menores (chunks) para assegurar que a recuperação traga o nível de detalhe adequado sem poluir o contexto.
2. **Indexação e Vetorização Semântica (`embeddinggemma`)**: O sistema utiliza o modelo de embeddings do Ollama para converter cada bloco de texto e as perguntas dos utilizadores em vetores numéricos de alta dimensionalidade que capturam o significado semântico das frases.
3. **Persistência Inteligente via Hash (`ChromaDB`)**: Para evitar o reprocessamento desnecessário dos embeddings a cada execução, a aplicação calcula uma assinatura digital com base em hash (`SHA256`) do conteúdo e do modelo. Caso os documentos não tenham sofrido alterações, a base vetorial persistente é reutilizada instantaneamente.  
4. **Recuperação por Similaridade e Geração (`phi4-mini`)**: Quando o utilizador digita uma pergunta no terminal, o sistema executa uma busca por similaridade de cosseno no ChromaDB para resgatar os dois trechos mais relevantes. Em seguida, injeta esse contexto recuperado na instrução (prompt) enviada ao modelo conversacional local, que redige a resposta final citando as fontes de origem e informando caso a informação esteja ausente.

---

## 3. Estrutura de Pastas do Módulo

A organização estrutural do módulo de RAG Vetorial é a seguinte:
```text
07_rag/
├── documentos/
│   ├── frequencia.md      # Regulamento fictício de controle de frequência.
│   ├── recuperacao.md     # Regulamento fictício para solicitações de recuperação.
│   └── revisao.md         # Regulamento fictício para revisão de avaliações.
├── banco_vetorial/        # Diretório persistente gerado pelo ChromaDB para armazenamento dos embeddings
├── comum.py               # Módulo utilitário contendo funções de leitura, limpeza de termos, chunking e resposta.
├── rag_vetorial.py        # Script principal que gerencia o ChromaDB, indexação e loop interativo de busca.
├── README.md              # Documentação oficial e descritiva do módulo.
└── requirements.txt       # Arquivo de dependências e bibliotecas necessárias.
```

---

## 4. Descrição dos Documentos da Base de conhecimento

base documental localizada na pasta `documentos` é composta por três arquivos em formato Markdown estruturados com diretrizes institucionais fictícias:  
- **frequencia.md**: Estabelece a regra principal de frequência mínima de 75% das aulas, o canal de consulta no portal acadêmico e o prazo limite de cinco dias úteis para a solicitação de correção de registros de presença junto ao docente.  
- **recuperacao.md**: Define as condições para estudantes com média inferior a 6 solicitarem atividades de recuperação no portal acadêmico em até sete dias corridos após a publicação da média, ressalvando que a recuperação não substitui o requisito obrigatório de frequência mínima.  
- **revisao.md**: Dispõe sobre o direito do estudante de solicitar a revisão de notas em até três dias úteis após a divulgação da avaliação, detalhando o procedimento de identificação de questões com justificativa objetiva no portal e advertindo que o processo pode resultar na manutenção ou alteração da nota.

---

## 5. Arquitetura e Papel dos Componentes do Código

O projeto está modularizado de forma a separar as responsabilidades de manipulação de dados, vetorização e geração textual:
- **comum.py**: Centraliza as funções fundamentais de suporte, incluindo a leitura dos documentos Markdown, a normalização de texto e remoção de stop words (termos), a recuperação textual por sobreposição de termos (buscar), o particionamento em blocos (chunks) e a interface de comunicação de fluxo com o modelo conversacional do Ollama (responder).
- **rag_vetorial.py**: Gerencia o ciclo de vida da base vetorial persistente utilizando o ChromaDB. Realiza o cálculo de uma assinatura digital baseada em hash SHA256 do conteúdo e do modelo para controlar o versionamento e a reutilização da coleção, gera os embeddings através do Ollama, executa as consultas por similaridade de cosseno e comanda o loop interativo no terminal.  
- **embeddinggemma**: Modelo de inteligência artificial responsável por converter os trechos textuais e as perguntas dos utilizadores em vetores numéricos densos de alta dimensionalidade, permitindo a recuperação semântica.
- **ChromaDB**: Banco de dados vetorial de execução local e persistente que armazena os embeddings gerados e indexa os dados para buscas rápidas por proximidade baseadas na distância de cosseno.
- **phi4-mini**: Modelo linguístico local executado via Ollama, encarregado de processar o contexto recuperado e redigir a resposta final em português, obedecendo estritamente às restrições de citação de fontes e de abstenção em caso de ausência de dados.

---

## 6. Instruções de Instalação e Execução

Para configurar e executar o módulo de RAG Vetorial em seu ambiente local, siga os passos abaixo:
1. **Pré-requisitos**: Certifique-se de possuir o Python 3.10 ou superior instalado, juntamente com o serviço do Ollama em execução no computador contendo os modelos `embeddinggemma` e `phi4-mini` descarregados.
2. **Instalação de Dependências**: Abra o terminal na pasta do módulo (`07_rag`) e instale os pacotes exigidos listados no ficheiro de configuração:
    ```bash
     pip install -r requirements.txt
    ```
3. Execute o script principal da aplicação:
     ```bash
     python rag_vetorial.py
     ```
4. **Interação**: O programa exibirá a quantidade de documentos e chunks carregados, informará o estado da base vetorial e abrirá um prompt interativo no terminal para que digite perguntas sobre os regulamentos acadêmicos.
 
---

## 7. Dificuldade Encontrada e Possível Melhoria

* **Dificuldade Encontrada:** Garantir que o particionamento (*chunking*) baseado estritamente em parágrafos não isolasse conceitos fundamentais de forma muito fragmentada, o que poderia gerar trechos curtos demais sem contexto suficiente para a vetorização semântica.
* **Possível Melhoria:** Implementar uma estratégia de particionamento com sobreposição de blocos (*sliding window/chunk overlap*), permitindo que partes finais de um parágrafo sejam repetidas no início do parágrafo seguinte, preservando a continuidade do contexto nas fronteiras dos trechos recuperados.
