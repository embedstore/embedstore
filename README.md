# embedstore

Python wrapper to access embeddings from [embedstore.ai](https://embedstore.ai)

# Install

```bash
git clone https://github.com/embedstore/embedstore.git
cd embedstore
python setup.py install
```

# APIS

## Load an embedding

```python
# load embeddings as a list
from embedstore import load_embedding

embeddings = load_embedding("9362fd4a-2653-4fe4-b931-9c83e7d6bf2c")
print(len(embeddings))
print(embeddings[1])

# load embeddings for ingesting in Chroma db
result = load_embedding("9362fd4a-2653-4fe4-b931-9c83e7d6bf2c", embed_for="chroma")
# result is {"embeddings": [], "documents": [] "ids": []}
print(result["embeddings"])
print(result["documents"])
print(result["ids"])
```

## Get all embeddings info

```python
from embedstore import get_embeddings_info

embeddings = get_embeddings_info()
```

## Get all embedding info

```python
from embedstore import search_embedding_info

embeddings = search_embedding_info("india")
```