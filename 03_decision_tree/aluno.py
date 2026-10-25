class Aluno:    
    def __init__(self, nome: str, media: float, frequencia: float, trabalhos_entregues: int, historico_reprovacao: int) -> None:
        self.nome = nome
        self.media = media
        self.frequencia = frequencia
        self.trabalhos_entregues = trabalhos_entregues
        self.historico_reprovacao = historico_reprovacao  