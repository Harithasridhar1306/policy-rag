from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub

def create_rag_chain(vectordb):
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-base"
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever()
    )
