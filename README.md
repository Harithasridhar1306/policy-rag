# Company Policy Chatbot (RAG)

A Retrieval-Augmented Generation chatbot that allows employees to ask
questions about company policy documents (HR, leave, onboarding, etc.).

## Architecture
PDF/DOCX → Chunking → Embeddings → Vector Store → Retrieval → LLM Answer

## Tech Stack
- Python
- LangChain
- HuggingFace Embeddings
- FAISS Vector Store
- Databricks (development)

## How It Works
1. Documents are loaded and converted to text
2. Text is split into chunks
3. Each chunk is embedded into vectors
4. Vectors are stored in FAISS
5. User query is embedded
6. Similar chunks are retrieved
7. LLM generates answer using retrieved context

## Run

pip install -r requirements.txt  
python app.py
