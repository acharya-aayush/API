from typing import Optional
from .schemas import Article, ArticleCreate

articles: list[Article] = [
    Article(id=1, title="Deploy checklist", body="Steps for a clean production release.", category="operations", tags=["release", "docs"])
]

_next_id = 2


def get_all_articles(category: Optional[str] = None) -> list[Article]:
    if category is None:
        return articles
    return [article for article in articles if article.category.lower() == category.lower()]


def get_article(article_id: int) -> Optional[Article]:
    return next((article for article in articles if article.id == article_id), None)


def create_article(payload: ArticleCreate) -> Article:
    global _next_id
    article = Article(id=_next_id, **payload.model_dump())
    articles.append(article)
    _next_id += 1
    return article
