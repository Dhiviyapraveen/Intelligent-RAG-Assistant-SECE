from app.services.retriever import retriever
from app.services.prompt_builder import prompt_builder
from app.services.llm import llm

from app.core.logger import logger


class RAGPipeline:

    def ask(self, question: str):

        logger.info(f"Question: {question}")

        # Step 1: Retrieve relevant chunks
        retrieved_chunks = retriever.retrieve(
            query=question,
            top_k=5
        )

        if len(retrieved_chunks) == 0:

            return {

                "answer": "I couldn't find that information on the official SECE website.",

                "sources": []

            }

        # Step 2: Build Prompt
        prompt = prompt_builder.build(
            question,
            retrieved_chunks
        )

        # Step 3: Generate Answer
        answer = llm.generate(prompt)

        # Step 4: Prepare Sources
        sources = []

        for chunk in retrieved_chunks:

            metadata = chunk["metadata"]

            source = {

                "title": metadata["title"],

                "url": metadata["url"]

            }

            if source not in sources:
                sources.append(source)

        return {

            "answer": answer,

            "sources": sources

        }


rag_pipeline = RAGPipeline()