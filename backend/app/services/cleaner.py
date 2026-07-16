import os
import json
import re

RAW_FOLDER = "data/raw"
CLEANED_FOLDER = "data/cleaned"


class DataCleaner:

    def __init__(self):
        os.makedirs(CLEANED_FOLDER, exist_ok=True)

    def clean_text(self, text):

        # Remove multiple spaces
        text = re.sub(r"\s+", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n+", "\n", text)

        # Remove common unwanted words
        remove_words = [
            "Skip to content",
            "Facebook",
            "Instagram",
            "Twitter",
            "LinkedIn",
            "YouTube"
        ]

        for word in remove_words:
            text = text.replace(word, "")

        return text.strip()

    def clean_all_pages(self):

        files = os.listdir(RAW_FOLDER)

        count = 0

        for file in files:

            if not file.endswith(".json"):
                continue

            path = os.path.join(RAW_FOLDER, file)

            with open(path, "r", encoding="utf-8") as f:
                document = json.load(f)

            cleaned_content = self.clean_text(document["content"])

            cleaned_document = {
                "url": document["url"],
                "title": document["title"],
                "content": cleaned_content
            }

            save_path = os.path.join(CLEANED_FOLDER, file)

            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(
                    cleaned_document,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

            count += 1

        return {
            "status": "success",
            "cleaned_files": count
        }


cleaner = DataCleaner()