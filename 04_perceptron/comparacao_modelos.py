from pathlib import Path
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import Perceptron
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


class MotorAnalise:
    def __init__(self, nome_instituicao: str) -> None:
        self.nome_instituicao = nome_instituicao
        self.modelo_arvore_decisao = DecisionTreeClassifier(random_state=42)
        self.modelo_perceptron = make_pipeline(
            StandardScaler(),
            Perceptron(random_state=42, max_iter=1000, tol=1e-3)
        )

    def carregar_dados(self, caminho_arquivo: str) -> pd.DataFrame:
        base_dir = Path(__file__).resolve().parent
        caminho = base_dir / caminho_arquivo
        return pd.read_csv(caminho)

    def treinar_e_avaliar(self, dados: pd.DataFrame) -> tuple:
        X = dados[["media", "frequencia"]]
        y = dados["risco"]

        X_treino, X_teste, y_treino, y_teste = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        self.modelo_arvore_decisao.fit(X_treino, y_treino)
        self.modelo_perceptron.fit(X_treino, y_treino)

        previsoes_teste_arvore = self.modelo_arvore_decisao.predict(X_teste)
        acuracia_arvore = accuracy_score(y_teste, previsoes_teste_arvore)

        previsoes_teste_perceptron = self.modelo_perceptron.predict(X_teste)
        acuracia_perceptron = accuracy_score(y_teste, previsoes_teste_perceptron)

        matriz_arvore = confusion_matrix(
            y_teste, previsoes_teste_arvore,
            labels=self.modelo_arvore_decisao.classes_
        )
        matriz_perceptron = confusion_matrix(
            y_teste, previsoes_teste_perceptron,
            labels=self.modelo_perceptron.classes_
        )

        return (
            acuracia_arvore,
            acuracia_perceptron,
            matriz_arvore,
            matriz_perceptron
        )

    def treinar_modelo_final(self, dados: pd.DataFrame) -> None:
        X = dados[["media", "frequencia"]]
        y = dados["risco"]

        self.modelo_arvore_decisao.fit(X, y)

    def prever_risco(self, media: float, frequencia: float) -> str:
        novo_aluno = pd.DataFrame({
            "media": [media],
            "frequencia": [frequencia]
        })
        previsao = self.modelo_arvore_decisao.predict(novo_aluno)
        return str(previsao[0])


def validar_entrada(mensagem: str,faixa_minima: int | float,faixa_maxima: int | float,tipo: type = float) -> int | float:
    while True:
        try:
            valor = tipo(input(mensagem))
            if faixa_minima <= valor <= faixa_maxima:
                return valor
            print(f"Erro: digite um número entre {faixa_minima} e {faixa_maxima}.")
        except ValueError:
            print("Erro: digite um valor numérico válido.")


def menu_prever_risco_aluno(motor: MotorAnalise) -> None:
    nome_aluno = input("\nNome do aluno: ").strip()
    media = validar_entrada("Média (0 a 10): ", 0.0, 10.0, float)
    frequencia = validar_entrada("Frequência (0 a 100): ", 0, 100, float)

    previsao_aluno = motor.prever_risco(media, frequencia)
    print(f"\nO aluno {nome_aluno} está na situação de: {previsao_aluno}.")
    input("\nPressione Enter para voltar...")


if __name__ == "__main__":
    motor = MotorAnalise("Universidade Exemplo")
    dados = motor.carregar_dados("data/dados_alunos.csv")

    print(f"Instituição: {motor.nome_instituicao}")
    print(f"- Base carregada com sucesso: {len(dados)} registros -")

    print("\n- COMPARAÇÃO: ÁRVORE DE DECISÃO X PERCEPTRON -")

    acuracia_arvore, acuracia_perceptron, matriz_arvore, matriz_perceptron = (
        motor.treinar_e_avaliar(dados)
    )

    print(f"\nAcurácia da Árvore de Decisão no conjunto de teste: {acuracia_arvore * 100:.1f}%")
    print("Matriz de Confusão da Árvore de Decisão:")
    print(matriz_arvore)

    print(f"\nAcurácia do Perceptron no conjunto de teste: {acuracia_perceptron * 100:.1f}%")
    print("Matriz de Confusão do Perceptron:")
    print(matriz_perceptron)

    motor.treinar_modelo_final(dados)

    print("\n- 3 PREVISÕES DE TESTE -\n")

    exemplos = [
        {"media": 8.5, "frequencia": 80.0},
        {"media": 5.0, "frequencia": 90.0},
        {"media": 4.0, "frequencia": 60.0}
    ]

    for ex in exemplos:
        resultado = motor.prever_risco(ex["media"], ex["frequencia"])
        print(
            f"Aluno com Média {ex['media']:.1f} e Frequência "
            f"{ex['frequencia']:.1f}% -> Diagnóstico Previsto: {resultado}"
        )

    print("-----------------------------------------------------------------------")

    continuar = True
    while continuar:
        opcao = input(
            "\nDeseja prever o risco de um novo aluno? [s/n]: "
        ).strip().casefold()

        match opcao:
            case "s":
                menu_prever_risco_aluno(motor)
            case "n":
                print("Encerrando o programa...")
                continuar = False
            case _:
                print("Opção inválida, digite novamente!")
