import re

import google.generativeai as genai

from google.generativeai.types import GenerationConfig

from app.core.config import settings
from app.core.logger import logger


class GeminiLLM:

    def __init__(self):

        logger.info("Initializing Gemini...")

        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash"
        )

        logger.info("Gemini Ready")

    def clean_response(self, text: str):

        text = text.replace("**", "")

        text = text.replace("*", "")

        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()

    def generate(self, prompt: str):

        try:

            response = self.model.generate_content(

                prompt,

                generation_config=GenerationConfig(

                    temperature=0.2,

                    top_p=0.8,

                    top_k=40,

                    max_output_tokens=512

                )

            )

            if not response.candidates:

                return "I couldn't find that information on the official SECE website."

            answer = response.text.strip()

            if answer == "":

                return "I couldn't find that information on the official SECE website."

            return self.clean_response(answer)

        except Exception as e:

            logger.error(f"Gemini Error : {str(e)}")

            return "Sorry, I am unable to answer your question at the moment."


llm = GeminiLLM()