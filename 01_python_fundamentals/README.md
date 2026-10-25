# Motor de Análise de Risco Acadêmico - Fundamentos

---

## 1. Objetivo do programa

Esta primeira versão do motor de análise de risco acadêmico foca nos fundamentos da linguagem Python. O programa processa e valida dados de desempenho estudantil utilizando estruturas básicas de controle e lógica iterativa.

---

## 2. Regras de Classificação de Risco

O sistema avalia a média e a frequência informadas, classificando o aluno nas seguintes categorias:
- **Risco alto**: média inferior a 6 e frequência inferior a 75%.
- **Risco baixo**: média igual ou superior a 6 e frequência igual ou superior a 75%.
- **Risco moderado**: quando apenas um dos dois critérios anteriores é atendido.

---

## 3. Como executar

Com o terminal aberto na raiz do repositório (python-ai-labs), execute o comando:
```bash
python 01_python_fundamentals/motor_analise_v1.py
```
O programa será iniciado no terminal, solicitando os dados do aluno e permitindo novas consultas até que você decida encerrar.