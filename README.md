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

embeddings = load_embedding("langchain/docs-python")
print(len(embeddings))
print(embeddings[1])

# load embeddings for ingesting in Chroma db
result = load_embedding("langchain/docs-python", embed_for="chroma")
# result is {"embeddings": [], "documents": [] "ids": []}
print(result["embeddings"])
print(result["documents"])
print(result["ids"])
```

## Get all embeddings info

```python
from embedstore import get_embeddings_info

embeddings = get_embeddings_info()

# output
{"data": [{"name": "The Almanack Of Naval Ravikant", "id": "book/naval-almanack"}, {"name": "Langchain Python Docs", "id": "langchain/docs-python"}]}
```

## Get all embedding info

```python
from embedstore import search_embedding_info

embeddings = search_embedding_info("doc")

# output
{"data": [{"name": "Langchain Python Docs", "id": "langchain/docs-python"}]}
```