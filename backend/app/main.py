from fastapi import FastAPI

from app.core.config import settings

from app.api.health import router as health_router
from app.api.chat import router as chat_router
from app.api.scrape import router as scrape_router
from app.api.index import router as index_router
from app.api.clean import router as clean_router
from app.api.chunk import router as chunk_router
from app.api.embed import router as embed_router
from app.api.search import router as search_router
from app.api.chat import router as chat_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="SECE Intelligent RAG Assistant"
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(scrape_router)
app.include_router(index_router)
app.include_router(clean_router)
app.include_router(chunk_router)
app.include_router(embed_router)
app.include_router(search_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }