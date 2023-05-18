# pyembeddingtown

Python wrapper to access embeddings from [embeddingtown.com](https://embeddingtown.com)

# Install

```bash
git clone https://github.com/taranjeet/pyembeddingtown.git
cd pyembeddingtown
python setup.py install
```

# APIS

## Download an embedding

```python
from pyembeddingtown import load_embedding

embeddings = load_embedding("9362fd4a-2653-4fe4-b931-9c83e7d6bf2c")

```

## Get all embedding info

```python
from pyembeddingtown import get_embeddings_info

embeddings = get_embeddings_info()
```

## Get all embedding info

```python
from pyembeddingtown import search_embedding_info

embeddings = search_embedding_info("india")
```