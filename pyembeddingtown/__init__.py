
from pyembeddingtown.apis import (
    get_embeddings_api,
    get_all_embeddings_api,
    search_embedding_doc_api,
)


def get_embeddings(doc_id):
    return get_embeddings_api(doc_id)


def get_embeddings_info():
    return get_all_embeddings_api()


def search_embedding_info(query):
    return search_embedding_doc_api(query)