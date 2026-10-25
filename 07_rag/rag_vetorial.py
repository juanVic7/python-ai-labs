import hashlib
import chromadb
import ollama
from comum import PASTA, chunks, responder, documentos

MODELO = "embeddinggemma"

def main() -> None:
    lista_docs = documentos()
    unidades = chunks()
  
    quantidade_documentos = len(lista_docs)
    quantidade_chunks = len(unidades)
    
    print(f"Quantidade de Documentos: {quantidade_documentos}")
    print(f"Quantidade de Chunks: {quantidade_chunks}")

    assinatura = hashlib.sha256(repr((MODELO, unidades)).encode()).hexdigest()[:16]

    banco = chromadb.PersistentClient(path=str(PASTA / "banco_vetorial"))
    colecao = banco.get_or_create_collection(
        name="tp07_" + assinatura, embedding_function=None,
        configuration={"hnsw": {"space": "cosine"}}
    )

    if colecao.count() == 0:
        vetores = ollama.embed(
            model=MODELO, 
            input=[t for _, t in unidades],
            truncate=False, 
            keep_alive=0
        )["embeddings"]
        
        colecao.add(
            ids=[f for f, _ in unidades], 
            documents=[t for _, t in unidades], 
            embeddings=vetores
        )
        print("Base indexada salva")
    else:
        print("Base indexada reutilizada")

    while pergunta := input("\nPergunta (Enter encerra): ").strip():
        print(f"\nPergunta: {pergunta}") 
        vetor = ollama.embed(model=MODELO, input=pergunta, keep_alive=0)["embeddings"]
        resultado = colecao.query(
            query_embeddings=vetor, 
            n_results=min(2, colecao.count()), 
            include=["documents", "distances"]
        )
        
        print("Distancias:", resultado["distances"][0])
        encontrados = list(zip(resultado["ids"][0], resultado["documents"][0]))
        
        for id_chunk, texto_chunk in encontrados:
            print(f"ID do chunk: {id_chunk}")
            print(f"Texto: {texto_chunk[:100]}...\n")
            
        responder(pergunta, encontrados)

if __name__ == "__main__":
    main()
