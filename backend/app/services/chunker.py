import os
import json

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.logger import logger

CLEANED_FOLDER = "data/cleaned"
CHUNK_FOLDER = "data/chunks"


class DocumentChunker:

    def __init__(self):

        os.makedirs(CHUNK_FOLDER, exist_ok=True)

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=800,

            chunk_overlap=150,

            separators=[
                "\n\n",
                "\n",
                ". ",
                "! ",
                "? ",
                " ",
                ""
            ]

        )

    def chunk_all_documents(self):

        files = os.listdir(CLEANED_FOLDER)

        total_chunks = 0

        total_documents = 0

        for file in files:

            if not file.endswith(".json"):
                continue

            path = os.path.join(CLEANED_FOLDER, file)

            with open(path, "r", encoding="utf-8") as f:

                document = json.load(f)

            text = document["content"]

            if len(text.strip()) == 0:
                continue

            chunks = self.splitter.split_text(text)

            chunk_objects = []

            for index, chunk in enumerate(chunks):

                chunk_objects.append({

                    "chunk_id": index,

                    "content": chunk

                })

            save_document = {

                "url": document["url"],

                "title": document["title"],

                "total_chunks": len(chunk_objects),

                "chunks": chunk_objects

            }

            save_path = os.path.join(CHUNK_FOLDER, file)

            with open(save_path, "w", encoding="utf-8") as f:

                json.dump(
                    save_document,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

            logger.info(
                f"{document['title']} -> {len(chunk_objects)} chunks"
            )

            total_chunks += len(chunk_objects)

            total_documents += 1

        return {

            "status": "success",

            "documents": total_documents,

            "chunks": total_chunks

        }


chunker = DocumentChunker()