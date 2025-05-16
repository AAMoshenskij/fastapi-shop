from fastapi import APIRouter, Query
from .services import search_products

router = APIRouter()

@router.get("/")
async def search(
    q: str = Query(...),
    category: str = None,
    min_rating: float = None
):
    return search_products(q, category, min_rating)
