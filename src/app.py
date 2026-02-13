from src.load_docs import load_docx
from src.chunk_docs import chunk_text
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.rag_chain import create_rag_chain

text = load_docx("data/sample_docs/policy.docx")
chunks = chunk_text(text)

embeddings = get_embeddings()
vectordb = create_vector_store(chunks, embeddings)

qa = create_rag_chain(vectordb)

while True:
    q = input("Ask: ")
    print(qa.run(q))
