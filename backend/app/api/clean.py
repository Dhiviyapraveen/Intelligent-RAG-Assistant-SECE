from fastapi import APIRouter

from app.services.cleaner import cleaner

router = APIRouter(
    prefix="/clean",
    tags=["Cleaner"]
)


@router.post("/")
def clean():

    return cleaner.clean_all_pages()