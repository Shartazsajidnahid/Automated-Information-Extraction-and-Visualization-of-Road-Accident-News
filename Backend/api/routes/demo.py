from fastapi import APIRouter
from ..controllers.b_nltk import stemming

router = APIRouter()

@router.get("/bnltk/")
def get_words():
    return stemming()