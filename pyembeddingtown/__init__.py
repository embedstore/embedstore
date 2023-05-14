
from pyembeddingtown.apis import (
    get_embeddings_api,
    get_all_embeddings_info,
)


def get_embeddings(doc_id):
    return get_embeddings_api(doc_id)


def get_embeddings_info():
    return get_all_embeddings_info()