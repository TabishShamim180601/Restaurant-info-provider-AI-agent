from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document 
import os
import pandas as pd

df = pd.read_csv("pizza_restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

#vector database location
db_location = "./chroma_langchain_db"

#checking if data has been vectorised before
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = [] #for list of documents in vector database
    ids = []       #for list of ids in vector database

    for i,row in df.iterrows():
        document = Document( 
            page_content=row["Title"] + " " + row["Review"], #helps in preserving context of query
            metadata={"rating":row["Rating"],"date":row["Date"]},
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name = "pizza_restaurant_reviews",
    persist_directory = db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents,ids=ids)

retriever = vector_store.as_retriever( 
    search_kwargs={"k":5} #pass 5 reviews as context to the llm

)