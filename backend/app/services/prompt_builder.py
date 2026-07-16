from app.core.prompts import SYSTEM_PROMPT


class PromptBuilder:

    def build(self, question, retrieved_chunks):

        context = ""

        for chunk in retrieved_chunks:

            metadata = chunk["metadata"]

            title = metadata["title"]

            context += f"\n\nPage : {title}\n"

            context += chunk["content"]

        return SYSTEM_PROMPT.format(

            context=context,

            question=question

        )


prompt_builder = PromptBuilder()