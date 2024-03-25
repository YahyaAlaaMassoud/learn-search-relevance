from tqdm.autonotebook import tqdm
from qdrant_client import QdrantClient, models


qdrant = QdrantClient(':memory:') # create in-mem instance of vector db
# qdrant = QdrantClient(
#     url=os.environ['QDRANT_URL'],
#     api_key=os.environ['QDRANT_API_KEY'],
# )


def build_index(passages, batch_size, start_idx, encoder, collection_name):
  collections_names = list(map(lambda x: x.name, qdrant.get_collections().collections))
  if collection_name in collections_names:
    print('collection is already there!')
    return

  qdrant.recreate_collection(
      collection_name=collection_name,
      vectors_config=models.VectorParams(
          size=encoder.get_sentence_embedding_dimension(),
          distance=models.Distance.COSINE,
          on_disk=True,
      ),
      optimizers_config=models.OptimizersConfigDiff(
          memmap_threshold=10000,
          default_segment_number=5,
          indexing_threshold=0,
      ),
      quantization_config=models.BinaryQuantization(
          binary=models.BinaryQuantizationConfig(always_ram=True),
      ),
  )

  passage_batch = []
  for idx, entry in enumerate(tqdm(passages[start_idx:], desc='Uploading vector embeddings in batch size of {}'.format(batch_size))):
    if len(passage_batch) < batch_size:
      passage_batch.append({
          'payload': entry,
          'id': idx + start_idx
      })
    else:
      passage_list = [item['payload']['passage'] for item in passage_batch]
      embedding_batch = encoder.encode(passage_list).tolist()
      records = [
          models.Record(
              id=entry['id'],
              payload=entry['payload'],
              vector=embedding
          ) for entry, embedding in zip(passage_batch, embedding_batch)
      ]
      qdrant.upload_records(
          collection_name=collection_name,
          records=records,
          parallel=10,
      )
      passage_batch = []

  return True
