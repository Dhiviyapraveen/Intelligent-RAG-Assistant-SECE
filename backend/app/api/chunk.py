from fastapi import APIRouter

from app.services.chunker import chunker

router = APIRouter(
    prefix="/chunk",
    tags=["Chunker"]
)


@router.post("/")
def chunk_documents():

    return chunker.chunk_all_documents()