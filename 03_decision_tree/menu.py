from aluno import Aluno
from motor_analise_v3 import MotorAnalise
import os

class Menu:
    def __init__(self, motor: MotorAnalise) -> None:
        self.motor = motor

    @staticmethod
    def validar_entrada(mensagem: str, faixa_minima: int | float, faixa_maxima: int | float, tipo: type = float) -> int | float:
        while True:
            try:
                valor = tipo(input(mensagem))
                if faixa_minima <= valor <= faixa_maxima:
                    return valor
                print(f"Erro: digite um número entre {faixa_minima} e {faixa_maxima}.")
            except ValueError:
                print("Erro: digite um valor numérico válido.")

    @staticmethod
    def limpar_tela() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def menu_cadastrar_aluno(self) -> None:
        continuar = True
        while continuar:
            print("=== CADASTRAR ALUNO ===\n")

            nome = input("Nome do aluno: ")
            media = self.validar_entrada("Média (0 a 10): ", 0.0, 10.0, float)
            frequencia = self.validar_entrada("Frequência (0 a 100): ", 0, 100, int)
            trabalhos_entregues = self.validar_entrada("Trabalhos entregues (0 a 5): ", 0, 5, int)
            historico_reprovacao = self.validar_entrada("Histórico de reprovação (0 a 1): ", 0, 1, int)

            novo_aluno = Aluno(nome, media, frequencia, trabalhos_entregues, historico_reprovacao)
            self.motor.cadastrar_aluno(novo_aluno)

            diagnostico = self.motor.prever_risco(novo_aluno)
            print(f"\nAluno cadastrado com sucesso! Diagnóstico: {diagnostico}\n")
            opcao = input("Digite 0 para sair ou qualquer tecla para cadastrar um novo aluno: ").strip()

            if opcao == "0":
                continuar = False
            else:
                self.limpar_tela()

    def menu_buscar_aluno(self) -> None:
        continuar = True
        while continuar:
            print("== BUSCAR ALUNO ==\n")

            if self.motor.lista_alunos:
                nome = input("Digite o nome do aluno: ")
                aluno_encontrado = self.motor.buscar_aluno_por_nome(nome)

                if aluno_encontrado is not None:
                    risco = self.motor.prever_risco(aluno_encontrado)
                    print("----------------------------------------------------------------------")
                    print(f"Aluno: {aluno_encontrado.nome}")
                    print(f"Média: {aluno_encontrado.media:.1f}")
                    print(f"Frequência: {aluno_encontrado.frequencia:.1f}%")
                    print(f"Trabalhos Entregues: {aluno_encontrado.trabalhos_entregues}")
                    print(f"Histórico de reprovação: {aluno_encontrado.historico_reprovacao}")
                    print(f"Classificação de risco: {risco}")
                    print("----------------------------------------------------------------------")
                else:
                    print("Aluno não encontrado!")
            else:
                print("Não há nenhum aluno cadastrado!")

            opcao = input("\nDigite 0 para sair ou qualquer tecla para fazer uma nova busca: ").strip()
            if opcao == "0":
                continuar = False
            else:
                self.limpar_tela()

    def menu_listar_alunos(self) -> None:
        print("== LISTA DE ALUNOS ==\n")

        if self.motor.lista_alunos:
            for aluno in self.motor.lista_alunos:
                risco = self.motor.prever_risco(aluno)
                print("----------------------------------------------------------------------")
                print(f"Aluno: {aluno.nome}")
                print(f"Média: {aluno.media:.1f}")
                print(f"Frequência: {aluno.frequencia}%")
                print(f"Trabalhos Entregues: {aluno.trabalhos_entregues}")
                print(f"Histórico de reprovação: {aluno.historico_reprovacao}")
                print(f"Classificação de risco: {risco}")
        else:
            print("Não há nenhum aluno cadastrado!")

        print("----------------------------------------------------------------------")
        input("\nPressione Enter para voltar ao menu...")
        self.limpar_tela()

    def menu_relatorios(self) -> None:
        print("== RELATÓRIOS ==")

        if self.motor.lista_alunos:
            print("-----------------------------------------------------------------------")
            qtd_alto, qtd_moderado, qtd_baixo = self.motor.calcular_qtd_por_classificacao()
            print(f"Alunos com Classificação de Risco Alto: {qtd_alto}")
            print(f"Alunos com Classificação de Risco Moderado: {qtd_moderado}")
            print(f"Alunos com Classificação de Risco Baixo: {qtd_baixo}\n")

            media_geral = self.motor.calcular_media_geral()
            print(f"Média Geral dos Alunos: {media_geral:.2f}\n")

            resultado_menor = self.motor.verificar_menor_frequencia()
            if resultado_menor:
                aluno, frequencia = resultado_menor
                print(f"Aluno com a menor frequência: {aluno} ({frequencia}%)")

            print("-----------------------------------------------------------------------")
        else:
            print("Não há nenhum dado para ser relatado!")

        input("\nPressione Enter para voltar ao menu...")
        self.limpar_tela()
