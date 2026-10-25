# Motor de Análise de Risco Acadêmico - IA Simbólica
---

## 1. Objetivo do programa

Esta segunda versão evolui o motor acadêmico incorporando conceitos de Inteligência Artificial Simbólica (ou IA baseada em regras). O programa utiliza uma base de conhecimento estruturada e regras lógicas explícitas para gerenciar múltiplos registros, processar estatísticas agregadas e realizar consultas automatizadas sobre o desempenho dos alunos.

---

## 2. Regras de Classificação de Risco

A análise é aplicada com base nas seguintes condições:

- **Risco Alto:** Média < 6.0 **e** Frequência < 75%
- **Risco Moderado:** Média < 6.0 **ou** Frequência < 75% (quando não atende ao critério de risco alto)
- **Risco Baixo:** Média >= 6.0 **e** Frequência >= 75%

---

## 3. Estrutura de Dados Utilizada e Contexto simbólico

Para simular uma base de fatos manipulada por um motor de inferência baseado em regras, foram implementadas as seguintes estruturas em Python:

- **Dicionário (`dict`):** Modela cada aluno individualmente com pares de chave-valor (`nome_aluno`, `media_aluno`, `frequencia_aluno` e `classificacao_risco`), garantindo clareza semântica e facilidade de acesso aos dados.
- **Lista (`list`):** Funciona como a base histórica de registros dentro da classe `MotorAnalise` (`self.lista_alunos`), permitindo iterações sequenciais para contagens, cálculos de média geral, busca de extremos e pesquisa por nome.

---

## 4. Principais Mudanças em Relação à Versão Anterior

1. **Persistência em Memória de Trabalho**: Diferente da versão anterior que analisava um único aluno por vez, esta versão armazena os dados em lote utilizando coleções.
2. **Motor de Consultas e Relatórios**: Adicionados métodos lógicos para calcular estatísticas gerais da turma (média da turma, contagem categorizada por nível de risco e identificação de o outlier de menor frequência).
3. **Interface Baseada em Menus e Decisão**: O fluxo principal foi transformado em um menu interativo acionado por escolhas (`match-case`), permitindo ao usuário navegar entre cadastro, listagem, relatórios e buscas customizadas.
4. **Busca Tolerante**: Implementação de tratamento de strings (`strip e casefold`) na busca por nomes para garantir robustez no casamento de símbolos.

---

## 5. Funcionalidades Implementadas

1. **Cadastro e Validação**: Entrada de múltiplos registros com validação estrita de faixas numéricas.
2. **Listagem de Registros**: Exibição formatada de toda a base de dados acumulada.
3. **Relatórios Estatísticos**: Consolidação automática de métricas de risco e desempenho geral.
4. **Busca por Nome**: Consulta indexada por string com tolerância a maiúsculas e minúsculas.

---

## 6. Como Executar

Com o terminal aberto na raiz do repositório (`python-ai-labs`), navegue até a pasta correspondente e execute o script:
```bash
python 02_simbolic_ai/motor_analise_v2.py
```
O programa iniciará o menu interativo no terminal, permitindo gerenciar os cadastros e consultar os relatórios gerados pelo motor simbólico.
