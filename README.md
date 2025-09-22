1. The project is an AI agent that utilises Retrieval Augmented Generation (RAG) pipeline to answer questions about a virtual pizza restaurant.
2. The RAG pipeline utilises LangChain ChromaDB. ChromaDB is used as the vector database. Llama3.2 is used as the large language model.  
3. For a provided question, the RAG pipeline embeds the question as a vector, fetches 5 similar vectors from the vector database and passes the embedded question and 5 vectors as context to the large language model.
4. To run the application:  
   A) Create a virtual environment  
   B) pip install -r requirements  
   C) run "python main.py"  
   
   
