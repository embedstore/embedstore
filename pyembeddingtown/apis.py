import ast
import csv
import requests
import tempfile

API_BASE_URL = "https://embeddingtown.com/"

API_ENDPOINT_GET_EMBEDDING_DOC = "api/embedding/v1/download/"
API_ENDPOINT_GET_ALL_EMBEDDING_INFO = "api/embedding/v1/info/"
API_ENDPOINT_SEARCH_EMBEDIDNG_DOC = "api/embedding/v1/search/"


def load_embedding_api(doc_id, embed_for=None):
    url = f"{API_BASE_URL}{API_ENDPOINT_GET_EMBEDDING_DOC}"
    data = {
        "doc_id": doc_id
    }
    if embed_for:
        data["embed_for"] = embed_for
    response = requests.post(url, data=data)
    if response.status_code == 200:
        if response.headers['Content-Type'] == 'application/json':
            json_data = response.json()
            return json_data
        elif response.headers['Content-Type'] == 'text/csv':
            with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as temp_file:
                temp_file.write(response.content)
                file_path = temp_file.name
            embeddings = []
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for idx, row in enumerate(csv_reader):
                    if idx == 0:
                        continue
                    embedding_str = row['embeddings']
                    embedding_list = ast.literal_eval(embedding_str)
                    embeddings.append(embedding_list)
            return embeddings
    else:
        raise Exception('Failed to fetch embeddings')


def get_all_embeddings_api():
    url = f"{API_BASE_URL}{API_ENDPOINT_GET_ALL_EMBEDDING_INFO}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch embeddings info")


def search_embedding_doc_api(query):
    url = f"{API_BASE_URL}{API_ENDPOINT_SEARCH_EMBEDIDNG_DOC}"
    params = {
        "query": query
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch embeddings info")