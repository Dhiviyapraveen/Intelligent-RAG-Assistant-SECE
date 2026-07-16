from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.rag_pipeline import rag_pipeline

router = APIRouter(

    prefix="/chat",

    tags=["RAG Chat"]

)


@router.post("/")

def chat(request: ChatRequest):

    return rag_pipeline.ask(

        request.question

    )