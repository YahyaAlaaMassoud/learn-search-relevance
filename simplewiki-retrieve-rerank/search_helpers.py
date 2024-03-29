import time

from qdrant_client import models


def retrieve_top_k(query, top_k, vec_db, encoder, collection_name):
  st = time.time()
  results = vec_db.search(
    collection_name=collection_name,
    query_vector=encoder.encode(query),
    limit=top_k,
    search_params=models.SearchParams(
      quantization=models.QuantizationSearchParams(
        ignore=False,
        rescore=True,
        oversampling=2.0,
      )
    )
  ) # search for top K passages from simplewiki
  query_time = time.time() - st

  top_hits = []
  for i, hit in enumerate(results):
    top_hits.append({'passage': hit.payload['passage'], 'article_id': hit.payload['article_id'], 'score': hit.score, 'order': (len(results) - i) / len(results)})

  return top_hits, query_time


def rerank_hits(query, hits, cross_encoder, articles):
  hits_order = {}
  for i, hit in enumerate(hits):
    hits_order[hit['article_id']] = i + 1

  cross_inp = [[query, hit['passage']] for hit in hits]
  st = time.time()
  cross_scores = cross_encoder.predict(cross_inp)
  hits_with_scores = list(zip(hits, cross_scores))
  sorted_hits = sorted(hits_with_scores, key=lambda x: x[1], reverse=True)
  reranking_time = time.time() - st
  reranked_hits = []
  for i, (hit, cross_score) in enumerate(sorted_hits):
    reranked_hits.append({
        'title': articles[hit['article_id']]['title'],
        'article_id': hit['article_id'],
        'passage': hit['passage'],
        'score': cross_score,
        'original_score': hit['score'],
        'retrieval_order': hits_order[hit['article_id']],
        'reranked_order': i + 1
    })
  return reranked_hits, reranking_time


def extract_sentence_and_partition(text, sentence):
    # Ensure the sentence exists in the text
    if sentence in text:
        # Find the start of the sentence
        start_index = text.find(sentence)
        # Find the end of the sentence
        end_index = start_index + len(sentence)
        # Extract parts
        before = text[:start_index]
        after = text[end_index:]
        # Return the partitioned list
        output = [(before, None), (sentence, "relevant passage"), (after, None)]
        if not len(before):
          output = output[1:]
        if not len(after):
          output = output[:-1]
        return output
    else:
        return ["", "", ""]  # Return empty strings if the sentence is not found


def fetch_top_article(hits, articles):
  if not hits:
    return None
  top_hit = hits[0]
  top_article = articles[top_hit['article_id']]['content']
  return top_article


def fetch_top_passage(hits):
  if not hits:
    return None
  return hits[0]['passage']


def fetch_top_article_with_passage_highlighted(hits, articles):
  if not hits:
    return None
  top_hit = hits[0]
  top_article = articles[top_hit['article_id']]['content']
  top_passage = top_hit['passage']
  return extract_sentence_and_partition(top_article, top_passage)
