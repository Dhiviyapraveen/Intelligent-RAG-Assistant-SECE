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

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        similarity_threshold: float = 1.2
    ):

        query_embedding = self.model.encode(
            query,
            normalize_embeddings=True
        ).tolist()

        results = collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k,

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

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            if distance > similarity_threshold:
                continue

            retrieved_chunks.append(

                {
                    "content": document,

                    "metadata": metadata,

                    "score": round(
                        1 - distance,
                        4
                    )

                }

            )

        retrieved_chunks.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        logger.info(
            f"Retrieved {len(retrieved_chunks)} relevant chunks."
        )

        return retrieved_chunks


retriever = Retriever()