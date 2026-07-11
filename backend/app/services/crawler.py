import requests
from bs4 import BeautifulSoup

from app.core.config import settings
from app.core.logger import logger


class WebsiteCrawler:

    def __init__(self):
        self.base_url = settings.SCRAPER_BASE_URL

    def crawl_homepage(self):

        logger.info(f"Crawling {self.base_url}")

        response = requests.get(self.base_url, timeout=10)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"

        page_text = soup.get_text(separator="\n", strip=True)

        logger.info("Homepage crawled successfully.")

        return {
            "url": self.base_url,
            "title": title,
            "content": page_text
        }


crawler = WebsiteCrawler()