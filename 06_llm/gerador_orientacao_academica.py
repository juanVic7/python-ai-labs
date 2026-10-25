from ollama import ResponseError, chat

DADOS_FICTICIOS = [
  {
    "nome" : "Marcos",
    "media" : 5.5,
    "frequencia" : 65,
    "situacao_informada" : "Estudante com dificuldade para organizar os estudos"
  },
  {
    "nome" : "Diego",
    "media" : 8.0,
    "frequencia" : 55,
    "situacao_informada" : "Estudante com boa média, mas dificuldade para manter a frequência"
  },
  {
    "nome" : "Paula",
    "media" : 9.0,
    "frequencia" : 80,
    "situacao_informada" : "Estudante com boa média e boa frequência, buscando manter a rotina"
  }  
]

class GeradorOrientacaoAcademica:
  def __init__(self, model: str = "phi4-mini") -> None:
    self.model = model
    
  def gerar_prompt(self, nome: str, media: float, frequencia: int, situacao: str) -> str:     
    return f"""
      Produza uma orientação acadêmica formal, natural e fluida para o estudante {nome}.
      Dados disponíveis:
      - Média: {media:.1f}
      - Frequência: {frequencia}%
      - Situação informada: {situacao}
      Regras para a resposta:
      - Responda obrigatoriamente em português do Brasil, utilizando linguagem correta e natural.
      - Escreva um texto curto, com no máximo 5 frases.
      - Use tom respeitoso, acolhedor e objetivo.
      - Apresente uma sugestão simples de organização dos estudos.
      - Incentive a reorganização da rotina de estudos.
      - Não invente disciplinas, professores, datas, regras ou informações pessoais.
      - Não use linguagem punitiva, ameaçadora ou discriminatória.
      """.strip()
 
  def gerar_orientacao(self, nome: str, media: float, frequencia: int, situacao: str) -> str:    
    prompt = self.gerar_prompt(nome = nome, media = media, frequencia = frequencia, situacao = situacao)
    try:
      resposta = chat(
        model = self.model,
        messages=[
          {
            "role" : "system",
            "content": """Você é um assistente acadêmico institucional que se comunica exclusivamente em português do Brasil.
            Utilize somente os dados fornecidos e siga rigorosamente todas as regras de solicitação.
            """,          
          },
          {
            "role" : "user",
            "content" : prompt,
          }
        ],
        options = {
          "temperature": 0.3,        
        },
      ) 
    except ResponseError:      
      return self.mensagem_fallback(nome)
      
    except Exception:
      return self.mensagem_fallback(nome)
   
    return self.validar_mensagem(mensagem=resposta.message.content, nome=nome)

  @staticmethod
  def validar_mensagem(mensagem: str, nome: str) -> str:
    mensagem = mensagem.strip()
    if not mensagem:
      return GeradorOrientacaoAcademica.mensagem_fallback(nome)
      
    if len(mensagem) > 600:
      mensagem = mensagem[:600].rsplit(" ", 1)[0] + "..."
    return mensagem

  @staticmethod
  def mensagem_fallback(nome: str) -> str:
    return f"""
    Olá, {nome}. Não foi possível gerar sua orientação personalizada 
    neste momento. Procure o apoio pedagógico da instituição para 
    conversar sobre seu desempenho e organizar sua rotina de estudos.     
    """

def main() -> None:
  gerador = GeradorOrientacaoAcademica(model="phi4-mini")

  for aluno in DADOS_FICTICIOS:
    mensagem_gerada = gerador.gerar_orientacao(aluno['nome'], aluno['media'], aluno['frequencia'], aluno['situacao_informada'])
    
    print(f"Estudante: {aluno['nome']}")
    print(f"Média: {aluno['media']}")
    print(f"Frequência: {aluno['frequencia']}")
    print(f"Situação informada: {aluno['situacao_informada']}")
    print("--- Mensagem gerada ---")
    print(mensagem_gerada)
    print("\n")
  
if __name__ == "__main__":
  main()
