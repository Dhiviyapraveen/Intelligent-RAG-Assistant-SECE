import os
import json

from sentence_transformers import SentenceTransformer

from app.database.vector_store import collection
from app.core.logger import logger

CHUNK_FOLDER = "data/chunks"


class Embedder:

    def __init__(self):

        logger.info("Loading Embedding Model...")

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        logger.info("Embedding Model Loaded Successfully")

    def embed_documents(self):

        files = os.listdir(CHUNK_FOLDER)

        embedded_chunks = 0

        for file in files:

            if not file.endswith(".json"):
                continue

            filepath = os.path.join(CHUNK_FOLDER, file)

            with open(filepath, "r", encoding="utf-8") as f:
                document = json.load(f)

            url = document["url"]
            title = document["title"]

            logger.info(f"Embedding -> {title}")

            for chunk in document["chunks"]:

                chunk_id = chunk["chunk_id"]
                chunk_text = chunk["content"]

                if not chunk_text.strip():
                    continue

                embedding = self.model.encode(
                    chunk_text,
                    normalize_embeddings=True
                ).tolist()

                collection.upsert(

                    ids=[
                        f"{file}_{chunk_id}"
                    ],

                    documents=[
                        chunk_text
                    ],

                    embeddings=[
                        embedding
                    ],

                    metadatas=[
                        {
                            "url": url,
                            "title": title,
                            "chunk_id": chunk_id,
                            "source": "SECE Website"
                        }
                    ]

                )

                embedded_chunks += 1

        return {

            "status": "success",

            "embedded_chunks": embedded_chunks

        }


embedder = Embedder()