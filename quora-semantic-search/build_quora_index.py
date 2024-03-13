import os

from tqdm import tqdm
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient, models


qdrant = QdrantClient(':memory:') # create in-mem instance of vector db
# qdrant = QdrantClient(
#     url=os.environ['QDRANT_URL'],
#     api_key=os.environ['QDRANT_API_KEY'],
# )
encoder = SentenceTransformer(model_name_or_path='BAAI/bge-small-en-v1.5')
MAX_QUESTIONS = 1000
BATCH_SIZE = 100


def compute_embedding(sentences, emb_model):
  return emb_model.encode(sentences=sentences)


def get_questions(ds):
  questions_text = set()
  for i, item in enumerate(ds):
    if i == MAX_QUESTIONS:
      break
    for q_text in item['questions']['text']:
      questions_text.add(q_text)
  unique_questions = list(questions_text)
  return [{'question': q} for q in unique_questions]


def build_index():
  collections_names = list(map(lambda x: x.name, qdrant.get_collections().collections))
  if 'questions' in collections_names:
    print('index is already there!')
    return
  
  quora_ds = load_dataset(path='quora', split='train', streaming=True)
  quora_questions = get_questions(ds=quora_ds)

  qdrant.recreate_collection(
      collection_name='questions',
      vectors_config=models.VectorParams(
          size=encoder.get_sentence_embedding_dimension(),
          distance=models.Distance.COSINE
      ),
      optimizers_config=models.OptimizersConfigDiff(
          memmap_threshold=200000 # optimize RAM usage https://qdrant.tech/documentation/concepts/storage/
      )
  )

  question_batch = []
  for idx, entry in enumerate(tqdm(quora_questions, desc='Uploading vector embeddings in batch size of {}'.format(BATCH_SIZE))):
    if len(question_batch) < BATCH_SIZE:
      question_batch.append({
          'payload': entry,
          'id': idx
      })
    else:
      questions_list = [item['payload']['question'] for item in question_batch]
      embedding_batch = compute_embedding(questions_list, encoder).tolist()
      records = [
          models.Record(
              id=entry['id'],
              payload=entry['payload'],
              vector=embedding
          ) for entry, embedding in zip(question_batch, embedding_batch)
      ]
      qdrant.upload_records(
          collection_name='questions',
          records=records
      )
      question_batch = []