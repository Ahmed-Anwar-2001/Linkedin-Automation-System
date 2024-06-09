from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.schema.runnable import RunnablePassthrough
from langchain.chains import LLMChain

import os
import requests
import pandas as pd
from sentence_transformers import SentenceTransformer, util


articles = ["https://www.linkedin.com/feed/update/urn:li:activity:7166333806944210944/",
            ]

# Scrapes the blogs above
loader = AsyncChromiumLoader(articles)
docs = loader.load()
#print(docs)
from langchain_community.document_transformers import Html2TextTransformer

html2text = Html2TextTransformer()
docs_transformed = html2text.transform_documents(docs)
#print(docs_transformed)

text_splitter = CharacterTextSplitter(chunk_size=100, 
                                      chunk_overlap=0)
chunked_documents = text_splitter.split_documents(docs_transformed)

# Load chunked documents into the FAISS index
db = FAISS.from_documents(chunked_documents, 
                          HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2'))

retriever = db.as_retriever()
print(retriever)


def get_query_vector(query, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    query_embedding = model.encode(query, convert_to_tensor=True)
    return query_embedding

def search_similar_documents(query_embedding, documents, top_k=5):
    similarity_scores = util.pytorch_cos_sim(query_embedding, documents)[0]
    sorted_indices = similarity_scores.argsort(descending=True)
    return sorted_indices[:top_k]
query_vector = get_query_vector('HR Intern') 
relevant_documents = retriever.get_relevant_documents(query_vector, top_k=5)  # Adjust top_k as needed

# Print relevant documents
for doc in relevant_documents:
    print("Relevant document:", doc)

