from fastapi import APIRouter

from app.services.crawler import crawler

router = APIRouter(
    prefix="/scrape",
    tags=["Scraper"]
)


@router.get("/")
def scrape_homepage():

    data = crawler.crawl_homepage()

    return {
        "message": "Homepage scraped successfully.",
        "data": data
    }