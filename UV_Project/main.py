from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

pdf_path = Path("./Info.pdf")

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

split_docs = text_splitter.split_documents(documents=docs)

embedder = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key = "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",
)

vector_store = QdrantVectorStore.from_documents(
    documents=[],
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder
)


vector_store.add_documents(documents=split_docs)
print("Injection Done")


retriver = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder
)

search_result = retriver.similarity_search(
    query="What is IOT?"
)

print("Relevant Chunks", search_result)