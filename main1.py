import os
from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from IPython.display import Markdown, display
from llama_index import StorageContext, load_index_from_storage

os.environ["OPENAI_API_KEY"] = "your-openapi-key"


documents = SimpleDirectoryReader("docs").load_data()


index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

user_query = input("Enter your question: ")

print(query_engine.query(user_query), "Thank you.")

index.storage_context.persist()

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context=storage_context)