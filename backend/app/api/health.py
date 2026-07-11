from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "Healthy",
        "message": "SECE Intelligent RAG Assistant is running"
    }