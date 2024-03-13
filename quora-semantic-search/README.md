### What You'll Find Here

- [`Quora Similar Questions Finder`](https://huggingface.co/spaces/yalaa/quora-similar-questions): Demo on Hugging Face 🤗 Space
- [`build_quora_index`](https://github.com/YahyaAlaaMassoud/learn-search-relevance/blob/main/tutorials/build_quora_index.py): Script that
  fetches the [Quora Duplicate Questions](https://huggingface.co/datasets/quora) dataset from Hugging Face [datasets](https://huggingface.co/datasets/)
  and creates a vector index using [Qdrant](https://qdrant.tech/) vector database by embedding the questions in the dataset using the [`BAAI/bge-small-en-v1.5`](https://huggingface.co/BAAI/bge-small-en-v1.5)
  provided by [SentenceTransformers](https://huggingface.co/sentence-transformers)
- [`quora_semantic_search.ipynb`](https://github.com/YahyaAlaaMassoud/learn-search-relevance/blob/main/tutorials/quora_semantic_search.ipynb): A step by step Jupyter notebook
  that implements semantic search on similar questions using Qdrant
- [`quora_semantic_search_gradio.ipynb`](https://github.com/YahyaAlaaMassoud/learn-search-relevance/blob/main/tutorials/quora_semantic_search_gradio.ipynb): A Jupyter
  notebook that creates a [Gradio](https://www.gradio.app/) app that find top K similar questions to an input query
