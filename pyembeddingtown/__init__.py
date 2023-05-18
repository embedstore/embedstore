
from pyembeddingtown.apis import (
    load_embedding_api,
    get_all_embeddings_api,
    search_embedding_doc_api,
)


def load_embedding(doc_id):
    return load_embedding_api(doc_id)


def get_embeddings_info():
    return get_all_embeddings_api()


def search_embedding_info(query):
    return search_embedding_doc_api(query)