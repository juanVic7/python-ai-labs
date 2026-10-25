import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


class MotorAnalise:
    def __init__(self, nome_instituicao: str) -> None:
        self.nome_instituicao = nome_instituicao
        self.lista_alunos = []  
  
    def exibir_nome_instituicao(self) -> None:
        print(f"Instituição: {self.nome_instituicao}")
  
    def avaliar_risco(self, media: float, frequencia: float) -> str:
        if media < 6.0 and frequencia < 75:           
            return "Risco alto"
        elif media < 6.0 or frequencia < 75:
            return "Risco moderado"
        else:
            return "Risco baixo"
          
    def cadastrar_aluno(self, nome: str, media: float, frequencia: int, classificacao_risco: str) -> None:        
        aluno = {            
            "nome_aluno": nome, 
            "media_aluno": media, 
            "frequencia_aluno":frequencia, 
            "classificacao_risco":classificacao_risco
        }
        self.lista_alunos.append(aluno)
      
    def calcular_qtd_por_classificacao(self) -> tuple[int, int, int]:        
        qtd_risco_baixo = 0
        qtd_risco_moderado = 0
        qtd_risco_alto = 0
      
        for aluno in self.lista_alunos:
            if aluno["classificacao_risco"] == "Risco alto":
                qtd_risco_alto = qtd_risco_alto + 1
          
            elif aluno["classificacao_risco"] == "Risco moderado":
                qtd_risco_moderado = qtd_risco_moderado + 1
          
            else:
                qtd_risco_baixo = qtd_risco_baixo + 1 
        return (qtd_risco_alto, qtd_risco_moderado, qtd_risco_baixo)
      
    def verificar_menor_frequencia(self) -> tuple[str, float]:
        aluno = self.lista_alunos[0]["nome_aluno"]
        menor_frequencia = self.lista_alunos[0]["frequencia_aluno"]
      
        for a in self.lista_alunos:
            if a["frequencia_aluno"] < menor_frequencia:
                aluno = a["nome_aluno"]
                menor_frequencia = a["frequencia_aluno"]
        return (aluno, menor_frequencia)

    def calcular_media_geral(self) -> float:
        soma = 0
        for aluno in self.lista_alunos:
            soma = soma + aluno["media_aluno"]
            media = soma/len(self.lista_alunos)
        return media
      
    def buscar_aluno_por_nome(self, nome: str) -> dict|None:
        nome = nome.strip().casefold()
        for aluno in self.lista_alunos:
            if aluno["nome_aluno"].strip().casefold() == nome:
                return aluno
        return None


def validar_entrada(mensagem: str, faixa_minima: int | float , faixa_maxima: int | float, tipo: type = float) -> int | float:    
    while True:       
        try:
            valor_digitado = tipo(input(mensagem))
            if(valor_digitado < faixa_minima or valor_digitado > faixa_maxima):
                print(f"Erro: digite um número dentro da faixa de {faixa_minima} a {faixa_maxima}\n")
            else:
                return valor_digitado
        except ValueError:
            print("Erro: digite um número válido\n")


def menu_cadastrar_alunos(motor: MotorAnalise) -> None:    
    continuar = True
    while(continuar):
        print("= CADASTRAR ALUNOS =\n")
    
        nome_aluno = input("Digite o nome do aluno: ")
        media_aluno = validar_entrada("Digite a média do aluno: ", 0.0, 10.0, float)
        frequencia_aluno = validar_entrada("Digite a frequência do aluno: ", 0, 100, int)
    
        classificacao_risco = motor.avaliar_risco(media_aluno, frequencia_aluno)
        print(f"Classificação de risco: {classificacao_risco}")
        motor.cadastrar_aluno(nome_aluno, media_aluno, frequencia_aluno, classificacao_risco)
    
        opcao = input("\nDigite 0 para sair ou qualquer tecla para cadastrar um novo aluno: ")
        if opcao == "0":           
            continuar = False
        limpar_tela()


def menu_listar_alunos(motor: MotorAnalise)-> None:
    limpar_tela()
    print("== LISTA DE ALUNOS ==\n")
  
    if motor.lista_alunos:
        for aluno in motor.lista_alunos:
          print("----------------------------------------------------------------------")
          print(f"Aluno: {aluno['nome_aluno']}")
          print(f"Média: {aluno['media_aluno']}")
          print(f"Frequência: {aluno['frequencia_aluno']}")
          print(f"Classificação de risco: {aluno['classificacao_risco']}")            
    else:   
        print("Não há nenhum aluno cadastrado!")
        
    print("----------------------------------------------------------------------")
    input("\npressione qualquer tecla para voltar ao menu")
    limpar_tela()  


def menu_relatorios(motor: MotorAnalise)-> None:
    print("== RELATÓRIOS ==\n")
    
    if motor.lista_alunos:
        print("-----------------------------------------------------------------------")
        qtd_alto, qtd_moderado, qtd_baixo = motor.calcular_qtd_por_classificacao()
        
        print(f"Alunos com Classificação de Risco Alta: {qtd_alto}")
        print(f"Alunos com Classificação de Risco Moderada: {qtd_moderado}")
        print(f"Alunos com Classificação de Risco Baixa: {qtd_baixo}\n")
        
        media_geral = motor.calcular_media_geral()
        print(f"Média Geral dos Alunos: {media_geral:.2f}\n")
        
        aluno, frequencia = motor.verificar_menor_frequencia()
        print(f"Aluno com a menor frequência: {aluno}({frequencia}%)")
        print("-----------------------------------------------------------------------")
        
    else:
        print("Não há nenhum dado para ser relatado!\n")
        
    input("pressione qualquer tecla para voltar ao menu")
    limpar_tela()


def menu_buscar_aluno(motor: MotorAnalise) -> None:
    continuar = True
    while continuar:
        print("== BUSCAR ALUNO ==\n")
        
        if motor.lista_alunos:
            nome = input("Digite o nome do aluno: ")
            aluno_encontrado = motor.buscar_aluno_por_nome(nome)
            
            if aluno_encontrado is not None:
                print("----------------------------------------------------------------------")
                print(f"Aluno: {aluno_encontrado['nome_aluno']}")
                print(f"Média: {aluno_encontrado['media_aluno']}")
                print(f"Frequência: {aluno_encontrado['frequencia_aluno']}")
                print(f"Classificação de risco: {aluno_encontrado['classificacao_risco']}")
                print("----------------------------------------------------------------------")
                
            else:
                print("Aluno não encontrado!")
        else:
            print("Não há nenhum aluno cadastrado!\n")
        opcao = input("Digite 0 para sair ou qualquer tecla para fazer uma nova busca: ")
        
        if opcao == "0":
            continuar = False
        limpar_tela()


def main() -> None:    
    continuar = True
    motor = MotorAnalise("Universidade Santa Cecília")
    while continuar:
        
        print("== MOTOR ANÁLISE ==\n")
        motor.exibir_nome_instituicao()
        
        print("\n[1] Cadastrar Aluno")
        print("[2] Alunos Cadastrados")
        print("[3] Relatório de Riscos")
        print("[4] Buscar Aluno por Nome")
        print("[0] Sair") 
        
        escolha = input("Escolha uma opcao: ")    
        match (escolha):
            case "1":
                limpar_tela()
                menu_cadastrar_alunos(motor)
            case "2":
                limpar_tela()
                menu_listar_alunos(motor)
            case "3":
                limpar_tela()
                menu_relatorios(motor)
            case "4":
                limpar_tela()
                menu_buscar_aluno(motor)
            case "0":
                print("Encerrando o programa...")
                continuar = False
            case _:
                input("Opção inválida, digite novamente!")
                limpar_tela()               


if __name__ == "__main__":
    main()
