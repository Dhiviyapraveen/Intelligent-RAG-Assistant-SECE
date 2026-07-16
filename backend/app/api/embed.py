from fastapi import APIRouter

from app.services.embedder import embedder

router = APIRouter(
    prefix="/embed",
    tags=["Embedding"]
)


@router.post("/")
def embed_documents():

    return embedder.embed_documents()