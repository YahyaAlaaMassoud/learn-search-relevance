import os
import json
import gzip

from sentence_transformers import util


def download_simplewiki(dataset_path):
  if not os.path.exists(dataset_path):
    util.http_get('https://sbert.net/datasets/{}'.format(dataset_path), dataset_path)


def get_all_passages(dataset_path):
  all_passages = []
  with gzip.open(dataset_path, 'rt', encoding='utf8') as fIn:
    for line in fIn:
      data = json.loads(line.strip())

      for passage in data['paragraphs']:
        all_passages.append({
            'passage': passage,
            'article_id': data['id']
        })
  return all_passages


def get_all_articles(dataset_path):
  all_articles = {}

  with gzip.open(dataset_path, 'rt', encoding='utf8') as fIn:
    for line in fIn:
      data = json.loads(line.strip())

      article = {
          'id': data['id'],
          'title': data['title'],
          'content': '\n'.join(data['paragraphs'])
      }
      all_articles[data['id']] = article

  return all_articles


def get_dataset(dataset_path):
  download_simplewiki(dataset_path)
  
  passages = get_all_passages(dataset_path)
  articles = get_all_articles(dataset_path)

  assert len(passages) == 509663
  assert len(articles) == 169597

  os.remove(dataset_path)

  return {
    'passages': passages,
    'articles': articles,
  }