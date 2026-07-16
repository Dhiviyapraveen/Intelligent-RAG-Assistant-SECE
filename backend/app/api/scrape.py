from fastapi import APIRouter

from app.services.crawler import crawler

router = APIRouter(
    prefix="/scrape",
    tags=["Scraper"]
)


@router.get("/")
def scrape():

    return crawler.crawl_all_pages()