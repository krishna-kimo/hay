#### API for COVID QandA
from haystack import Finder
from haystack.indexing.cleaning import clean_wiki_text
from haystack.indexing.io import write_documents_to_db, fetch_archive_from_http
from haystack.reader.farm import FARMReader
from haystack.reader.transformers import TransformersReader

## Document Store
from haystack.database.elasticsearch import ElasticsearchDocumentStore

## Retriver
from haystack.retriever.elasticsearch import ElasticsearchRetriever
## config details
from config import DB_HOST, DB_USER, DB_PW, DB_INDEX
from config import READER_MODEL_PATH
from fastapi import FastAPI
from pydantic import BaseModel

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


app = FastAPI()
### Model values for Reader and Document Store
global document_store, retriever, reader, finder
document_store = ElasticsearchDocumentStore(host=DB_HOST, username=DB_USER, password=DB_PW, index=DB_INDEX)
retriever = ElasticsearchRetriever(document_store=document_store)
reader = FARMReader(model_name_or_path=READER_MODEL_PATH, use_gpu=False)
finder = Finder(reader, retriever)

## API

class Item(BaseModel):
    query: str


@app.get("/greet")
async def greet():
    return {"message": "Hi there!!! I am working"}

@app.post("/ask")
async def predict(item: Item):
    
    question = item.query
    top_k_retriever=5
    top_k_reader=5

    prediction = finder.get_answers(question=question, top_k_retriever=5, top_k_reader=5)
    
    res = {}
    res['response'] = prediction
    return res
