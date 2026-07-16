from app.core.prompts import SYSTEM_PROMPT


class PromptBuilder:

    def build(
        self,
        question: str,
        retrieved_chunks: list
    ):

        context_parts = []

        for index, chunk in enumerate(
            retrieved_chunks,
            start=1
        ):

            metadata = chunk["metadata"]

            score = chunk["score"]

            section = f"""
==========================
SOURCE {index}

Title:
{metadata["title"]}

URL:
{metadata["url"]}

Similarity Score:
{score}

Content:
{chunk["content"]}

==========================
"""

            context_parts.append(section)

        context = "\n".join(context_parts)

        prompt = SYSTEM_PROMPT.format(

            context=context,

            question=question

        )

        return prompt


prompt_builder = PromptBuilder()