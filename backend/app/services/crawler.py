import os
import json
import hashlib
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

from app.core.config import settings
from app.core.logger import logger


RAW_FOLDER = "data/raw"


class WebsiteCrawler:

    def __init__(self):
        self.base_url = settings.SCRAPER_BASE_URL

        self.skip_keywords = [
            "slot-gacor",
            "things-to-do",
            "casino",
            "poker",
            "bet",
            "login"
        ]

        os.makedirs(RAW_FOLDER, exist_ok=True)

    def crawl_homepage(self):

        logger.info(f"Crawling {self.base_url}")

        response = requests.get(self.base_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"

        links = self.extract_internal_links(soup)

        return {
            "url": self.base_url,
            "title": title,
            "total_links": len(links),
            "links": sorted(list(links))
        }

    def extract_internal_links(self, soup):

        internal_links = set()

        base_domain = urlparse(self.base_url).netloc

        for tag in soup.find_all("a", href=True):

            href = tag["href"]

            full_url = urljoin(self.base_url, href)

            parsed = urlparse(full_url)

            if parsed.netloc != base_domain:
                continue

            if parsed.path.endswith(".pdf"):
                continue

            if any(word in parsed.path.lower() for word in self.skip_keywords):
                continue

            cleaned_url = parsed.scheme + "://" + parsed.netloc + parsed.path

            internal_links.add(cleaned_url)

        return internal_links

    def save_page(self, url, title, content):

        # unique filename using md5 hash
        filename = hashlib.md5(url.encode()).hexdigest() + ".json"

        filepath = os.path.join(RAW_FOLDER, filename)

        document = {
            "url": url,
            "title": title,
            "content": content,
            "scraped_at": datetime.now().isoformat()
        }

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(
                document,
                file,
                indent=4,
                ensure_ascii=False
            )

        logger.info(f"Saved -> {filename}")

    def crawl_all_pages(self):

        homepage = self.crawl_homepage()

        links = homepage["links"]

        total = len(links)

        success = 0
        failed = 0

        for index, link in enumerate(links, start=1):

            try:

                logger.info(f"[{index}/{total}] {link}")

                response = requests.get(link, timeout=10)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "html.parser")

                title = soup.title.string.strip() if soup.title else "No Title"

                content = soup.get_text(separator="\n", strip=True)

                self.save_page(link, title, content)

                success += 1

            except Exception as e:

                failed += 1

                logger.error(f"Failed -> {link}")

                logger.error(str(e))

        return {
            "status": "completed",
            "total_links": total,
            "saved_pages": success,
            "failed_pages": failed
        }


crawler = WebsiteCrawler()