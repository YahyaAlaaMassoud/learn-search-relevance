# search-relevance

## datasets

- [`quora`](https://huggingface.co/datasets/quora): The Quora dataset is composed of question pairs, and the task is to determine if the questions are paraphrases of each other (have the same meaning).
- [`wiki`](https://www.dropbox.com/scl/fi/yxzmsrv2sgl249zcspeqb/lesson2-wiki.csv.zip?rlkey=paehnoxjl3s5x53d1bedt4pmc&e=1&dl=0%22): From DeepLearning.ai Building Applications with Vector Databases Course.
  ```
  !wget -q -O lesson2-wiki.csv.zip "https://www.dropbox.com/scl/fi/yxzmsrv2sgl249zcspeqb/lesson2-wiki.csv.zip?rlkey=paehnoxjl3s5x53d1bedt4pmc&dl=0"
  !unzip lesson2-wiki.csv.zip
  ```
- [`news`](https://www.dropbox.com/scl/fi/wruzj2bwyg743d0jzd7ku/all-the-news-3.zip?rlkey=rgwtwpeznbdadpv3f01sznwxa&e=1&dl=1%22): From DeepLearning.ai Building Applications with Vector Databases Course.
  ```
  wget -q --show-progress -O all-the-news-3.zip "https://www.dropbox.com/scl/fi/wruzj2bwyg743d0jzd7ku/all-the-news-3.zip?rlkey=rgwtwpeznbdadpv3f01sznwxa&dl=1"
  unzip all-the-news-3.zip
  ```
- [`ashraq/fashion-product-images-small`](https://huggingface.co/datasets/ashraq/fashion-product-images-small): Multimodal data of fashion products
- [`family-photos`](https://www.dropbox.com/scl/fi/yg0f2ynbzzd2q4nsweti5/family_photos.zip?rlkey=00oeuiii3jgapz2b1bfj0vzys&dl=0): From DeepLearning.ai Building Applications with Vector Databases Course.
  ```
  !wget -q --show-progress -O family_photos.zip "https://www.dropbox.com/scl/fi/yg0f2ynbzzd2q4nsweti5/family_photos.zip?rlkey=00oeuiii3jgapz2b1bfj0vzys&dl=0"
  !unzip -q family_photos.zip
  ```
- [`cisco-logs`](https://www.dropbox.com/scl/fi/rihfngx4ju5pzjzjj7u9z/lesson6.tar.zip?rlkey=rct9a9bo8euqgshrk8wiq2orh&dl=1): From DeepLearning.ai Building Applications with Vector Databases Course.
  ```
  !wget -q --show-progress -O training.tar.zip "https://www.dropbox.com/scl/fi/rihfngx4ju5pzjzjj7u9z/lesson6.tar.zip?rlkey=rct9a9bo8euqgshrk8wiq2orh&dl=1"
  !tar -xzvf training.tar.zip
  !tar -xzvf lesson6.tar
  ```

## tools
- [`DSPy`](https://github.com/stanfordnlp/dspy): For programming - not prompting - LLMs
- [`jinja2`](https://pypi.org/project/Jinja2/): For creating prompt templates
- [`python-dotenv`](https://github.com/theskumar/python-dotenv): For loading .env variables
- [`poetry`](https://github.com/python-poetry/poetry): For Python package and dep management
- [`uv`](https://github.com/astral-sh/uv): Package installer written in Rust
- [`ruff`](https://github.com/astral-sh/ruff): Fast Python linter and code formatter
