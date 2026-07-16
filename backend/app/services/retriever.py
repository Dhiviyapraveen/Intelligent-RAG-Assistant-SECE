from sentence_transformers import SentenceTransformer

from app.database.vector_store import collection
from app.core.logger import logger


class Retriever:

    def __init__(self):

        logger.info("Loading Retrieval Model...")

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        logger.info("Retriever Ready")

    def normalize_url(self, url: str):

        if url.endswith("/"):
            url = url[:-1]

        return url

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        similarity_threshold: float = 1.10
    ):

        logger.info(f"Searching for: {query}")

        query_embedding = self.model.encode(
            query,
            normalize_embeddings=True
        ).tolist()

        # Retrieve more candidates first
        results = collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k * 3,

            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        retrieved_chunks = []

        seen_urls = set()

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            if distance > similarity_threshold:
                continue

            url = self.normalize_url(
                metadata["url"]
            )

            # Skip duplicate pages
            if url in seen_urls:
                continue

            seen_urls.add(url)

            score = round(1 - distance, 4)

            retrieved_chunks.append(

                {
                    "content": document,
                    "metadata": {
                        "title": metadata["title"],
                        "url": url,
                        "source": metadata.get("source", "SECE Website"),
                        "chunk_id": metadata.get("chunk_id", 0)
                    },
                    "score": score
                }

            )

            if len(retrieved_chunks) >= top_k:
                break

        logger.info(
            f"Retrieved {len(retrieved_chunks)} unique chunks."
        )

        return retrieved_chunks


retriever = Retriever()