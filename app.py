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

from flask import Flask, request, Response, jsonify
import logging
import gunicorn

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
## util functions

def init():
    ### Model values for Reader and Document Store
    global document_store, retriever, reader, finder
    document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document")
    retriever = ElasticsearchRetriever(document_store=document_store)
    reader = FARMReader(model_name_or_path='deepset/roberta-base-squad2-covid', use_gpu=False)
    finder = Finder(reader, retriever)

## API

@app.route("/greet")
def greet():
    return jsonify("Hello there!! I am working")

@app.route("/writedb", methods=['POST'])
def write_to_db():
    try:
        ## TODO: Get DOCS_DIR from config

        write_documents_to_db(document_store=document_store, document_dir=doc_dir, \
                      only_empty_db=True, split_paragraphs=True)

        return True
    except :
        return jsonify("Can not write to DB")

@app.route("/ask", methods=['POST'])
def predict():
    req = request.get_json()
    top_k_retriever=5
    top_k_reader=5
    question = req['q']

    prediction = finder.get_answers(question=question, top_k_retriever=5, top_k_reader=5)

    return jsonify(prediction)


### Main
if __name__ == "__main__":
    app.logger.info("Initialising the models....")
    init()
    app.logger.info("Model Loading done...")
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)

