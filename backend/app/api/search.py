from fastapi import APIRouter

from app.services.retriever import retriever

router = APIRouter(
    prefix="/search",
    tags=["Retriever"]
)


@router.get("/")
def search(

    query: str,

    top_k: int = 5

):

    return retriever.retrieve(
        query=query,
        top_k=top_k
    )