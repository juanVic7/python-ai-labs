import pandas as pd
from pathlib import Path
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def validar_entrada(mensagem: str, faixa_minima: int | float, faixa_maxima: int | float, tipo: type = float) -> int | float:
    while True:
        try:
            valor_digitado = tipo(input(mensagem))
            if valor_digitado < faixa_minima or valor_digitado > faixa_maxima:
                print(f"Erro: digite um número dentro da faixa de {faixa_minima} a {faixa_maxima}\n")
            else:
                return valor_digitado
        except ValueError:
            print("Erro: digite um número válido\n")


class MotorAnalise:
    def __init__(self, nome_instituicao: str) -> None:
        self.nome_instituicao = nome_instituicao
        self.scaler = StandardScaler()
        self.modelo = MLPClassifier(hidden_layer_sizes=(5,), activation="relu", max_iter=2000, random_state=42)

    def carregar_dados(self, caminho_arquivo: str) -> pd.DataFrame:
        base_dir = Path(__file__).resolve().parent
        caminho = base_dir / caminho_arquivo
        return pd.read_csv(caminho)

    def treinar_modelo(self, dados: pd.DataFrame) -> tuple:
        X = dados[["media", "frequencia", "trabalhos_entregues", "historico_reprovacao"]]
        y = dados["risco"]

        X_treino, X_teste, y_treino, y_teste = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        X_treino_escalado = self.scaler.fit_transform(X_treino)
        X_teste_escalado = self.scaler.transform(X_teste)

        self.modelo.fit(X_treino_escalado, y_treino)

        previsoes_modelo = self.modelo.predict(X_teste_escalado)
        acuracia_modelo = accuracy_score(y_teste, previsoes_modelo)

        matriz_modelo = confusion_matrix(
            y_teste, previsoes_modelo, labels=self.modelo.classes_
        )

        return acuracia_modelo, matriz_modelo

    def prever_risco(self, media: float, frequencia: int, trabalhos_entregues: int, historico_reprovacao: int) -> str:
        novo_aluno = pd.DataFrame([{
            "media": media,
            "frequencia": frequencia,
            "trabalhos_entregues": trabalhos_entregues,
            "historico_reprovacao": historico_reprovacao
        }])

        novo_aluno_escalado = self.scaler.transform(novo_aluno)
        predicao = self.modelo.predict(novo_aluno_escalado)

        return str(predicao[0])


def main() -> None:
    motor = MotorAnalise("Universidade Exemplo")
    dados = motor.carregar_dados("data/dados_alunos.csv")

    print("--- Dados carregados ---")
    print(dados)

    acuracia, matriz_confusao = motor.treinar_modelo(dados)

    print(f"\nAcurácia do MLPClassifier no conjunto de teste: {acuracia * 100:.1f}%")
    print("Matriz de Confusão do MLPClassifier:")
    print(matriz_confusao)

    continuar = True
    print("--- Previsão com rede neural multicamada ---")

    while continuar:
        media = validar_entrada("Média (0 a 10): ", 0.0, 10.0, float)
        frequencia = validar_entrada("Frequência (0 a 100): ", 0, 100, int)
        trabalhos_entregues = validar_entrada("Trabalhos entregues (0 a 5): ", 0, 5, int)
        historico_reprovacao = validar_entrada("Histórico de reprovação (0 ou 1): ", 0, 1, int)

        risco = motor.prever_risco(media, frequencia, trabalhos_entregues, historico_reprovacao)
        print(f"\nRisco previsto: {risco}")

        opcao = input("Digite 0 para sair ou qualquer tecla para uma nova previsão: ").strip()

        if opcao == "0":
            print("Encerrando o programa...")
            continuar = False
        else:
            limpar_tela()


if __name__ == "__main__":
    main()
