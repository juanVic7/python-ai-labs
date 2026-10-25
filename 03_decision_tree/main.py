from menu import Menu
from motor_analise_v3 import MotorAnalise

def main() -> None:
    continuar = True
    motor = MotorAnalise("Universidade Exemplo")
    dados = motor.carregar_dados("data/dados_alunos.csv")
    print("--- Dados carregados ---")
    print(dados)
    motor.treinar_modelo(dados)
    menu = Menu(motor)

    while continuar:
        print("== MOTOR ANÁLISE ==\n")
        motor.exibir_nome_instituicao()
        print("\n[1] Cadastrar Aluno")
        print("[2] Alunos Cadastrados")
        print("[3] Relatório de Riscos")
        print("[4] Buscar Aluno por Nome")
        print("[0] Sair")
        escolha = input("Escolha uma opção: ").strip()

        match escolha:
            case "1":
                menu.limpar_tela()
                menu.menu_cadastrar_aluno()
            case "2":
                menu.limpar_tela()
                menu.menu_listar_alunos()
            case "3":
                menu.limpar_tela()
                menu.menu_relatorios()
            case "4":
                menu.limpar_tela()
                menu.menu_buscar_aluno()
            case "0":
                print("Encerrando o programa...")
                continuar = False
            case _:
                input("Opção inválida, digite novamente!")
                menu.limpar_tela()


if __name__ == "__main__":
    main()
