# Search Relevance Repository 🔍

I created this repository to explore various search relevance techniques by developing tutorials 🏗️, creating Hugging Face 🤗 spaces and demos, and compiling useful resources 📚.

### List of tutorials 📖
- [`Quora Similar Questions Finder`](https://yalaa-quora-similar-questions.hf.space): Hugging Face 🤗 Space. A demonstration of constructing a vector index database with Qdrant using questions from Quora. It then employs semantic search to identify the top K questions most similar to the user's input.
- [`Semantic Search on Simple Wikipedia Through Retrieval and Reranking`](https://huggingface.co/spaces/yalaa/simplewiki-retrieve-rerank): Hugging Face 🤗 Space. Based on the user's input question or query, the algorithm searches through ~250k passages to find the top K relevant passages to the query, then reranks the results and outputs the top article with the relevant passage highlighted. Qdrant is used as a vector store, and SentenceTransformers are used for generating embeddings and reranking through cross-encoders. Finally, the demo is powered by Gradio.

### Contributing 💡
Feel free to contribute by sharing your insights, improvements, or any useful resources related to search relevance.

### Stay Connected 🤝
Star or watch this repository for updates on new tutorials and resources. Your support helps this project grow.
