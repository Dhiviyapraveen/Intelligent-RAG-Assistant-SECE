from fastapi import APIRouter

router = APIRouter(
    prefix="/index",
    tags=["Indexer"]
)


@router.post("/")
def index():
    return {
        "message": "Indexing endpoint is ready."
    }