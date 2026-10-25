from aluno import Aluno
import pandas as pd
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier

class MotorAnalise:
    def __init__(self, nome_instituicao: str) -> None:
        self.nome_instituicao = nome_instituicao
        self.lista_alunos = []
        self.modelo = DecisionTreeClassifier(random_state=42)

    def exibir_nome_instituicao(self) -> None:
        print(f"Instituição: {self.nome_instituicao}")

    def carregar_dados(self, caminho_arquivo: str) -> pd.DataFrame:
        base_dir = Path(__file__).resolve().parent
        caminho = base_dir / caminho_arquivo
        return pd.read_csv(caminho)

    def treinar_modelo(self, dados: pd.DataFrame) -> None:
        X = dados[["media", "frequencia", "trabalhos_entregues", "historico_reprovacao"]]
        y = dados["risco"]
        self.modelo.fit(X, y)

    def prever_risco(self, aluno: Aluno) -> str:
        dados_aluno = pd.DataFrame([{
            "media": aluno.media,
            "frequencia": aluno.frequencia,
            "trabalhos_entregues": aluno.trabalhos_entregues,
            "historico_reprovacao": aluno.historico_reprovacao
        }])
        predicao = self.modelo.predict(dados_aluno)
        return str(predicao[0])

    def cadastrar_aluno(self, aluno: Aluno) -> None:
        self.lista_alunos.append(aluno)

    def calcular_qtd_por_classificacao(self) -> tuple[int, int, int]:
        qtd_risco_alto = 0
        qtd_risco_moderado = 0
        qtd_risco_baixo = 0

        for aluno in self.lista_alunos:
            diagnostico = self.prever_risco(aluno)

            if diagnostico == "alto":
                qtd_risco_alto += 1
            elif diagnostico == "moderado":
                qtd_risco_moderado += 1
            else:
                qtd_risco_baixo += 1

        return (qtd_risco_alto, qtd_risco_moderado, qtd_risco_baixo)

    def verificar_menor_frequencia(self) -> tuple[str, float] | None:
        if not self.lista_alunos:
            return None

        aluno = self.lista_alunos[0].nome
        menor_frequencia = self.lista_alunos[0].frequencia

        for a in self.lista_alunos:
            if a.frequencia < menor_frequencia:
                aluno = a.nome
                menor_frequencia = a.frequencia

        return (aluno, menor_frequencia)

    def calcular_media_geral(self) -> float:
        if not self.lista_alunos:
            return 0.0

        soma = 0.0
        for aluno in self.lista_alunos:
            soma += aluno.media

        return soma / len(self.lista_alunos)

    def buscar_aluno_por_nome(self, nome: str) -> Aluno | None:
        nome = nome.strip().casefold()
        for aluno in self.lista_alunos:
            if aluno.nome.strip().casefold() == nome:
                return aluno
        return None
