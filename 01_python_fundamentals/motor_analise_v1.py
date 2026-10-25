import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


class MotorAnalise:
    def __init__(self, nome_instituicao: str) -> None:
        self.nome_instituicao = nome_instituicao
    
    def exibir_nome_instituicao(self) -> None:
        print(f"Instituição: {self.nome_instituicao}\n")
    
    def avaliar_risco(self, media: float, frequencia: int) -> str:
        if media < 6.0 and frequencia < 75:           
            return "Risco alto"
        elif media >= 6.0 and frequencia >= 75:
            return "Risco baixo"
        else:
            return "Risco moderado"


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


def main() -> None:
    continuar = True
    motor = MotorAnalise("Universidade Exemplo")
    while continuar:
        motor.exibir_nome_instituicao()
        nome_aluno = input("Digite o nome do aluno: ")
        media_aluno = validar_entrada("Digite a média do aluno: ", 0.0, 10.0, float)
        frequencia_aluno = validar_entrada("Digite a frequência do aluno: ", 0, 100, int)
        classificacao_risco = motor.avaliar_risco(media_aluno, frequencia_aluno)

        print("\n--- Resultado da análise ---")
        print(f"Aluno: {nome_aluno}")
        print(f"Média: {media_aluno:.2f}")
        print(f"Frequência: {frequencia_aluno}%")
        print(f"Classificação de risco: {classificacao_risco}")
    
        opcao = input("\nAperte 0 para sair ou qualquer tecla para continuar: ")
        if opcao == "0":
            print("Encerrando o programa...")
            continuar = False
        else:
            limpar_tela()


if __name__ == "__main__":
    main()
  