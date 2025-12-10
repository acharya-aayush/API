from fastapi import APIRouter, HTTPException
from .schemas import Article, ArticleCreate
from .services import get_all_articles, get_article, create_article

router = APIRouter()

@router.get("/", response_model=list[Article])
def list_articles(category: str | None = None):
    return get_all_articles(category)

@router.get("/{article_id}", response_model=Article)
def read_article(article_id: int):
    article = get_article(article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.post("/", response_model=Article, status_code=201)
def create_article_endpoint(payload: ArticleCreate):
    return create_article(payload)
