
from pyembeddingtown.apis import get_embeddings_api


def get_embeddings(doc_id):
    return get_embeddings_api(doc_id)
