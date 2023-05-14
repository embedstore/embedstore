import ast
import csv
import requests
import tempfile

API_BASE_URL = "https://embeddingtown.com/"

API_ENDPOINT_GET_EMBEDDING_DOC = "api/embedding/v1/download/"
API_ENDPOINT_GET_ALL_EMBEDDING_INFO = "api/embedding/v1/info/"


def get_embeddings_api(doc_id):
    url = f"{API_BASE_URL}{API_ENDPOINT_GET_EMBEDDING_DOC}"
    data = {
        "doc_id": doc_id
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
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


def get_all_embeddings_info():
    url = f"{API_BASE_URL}{API_ENDPOINT_GET_ALL_EMBEDDING_INFO}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch embeddings info")