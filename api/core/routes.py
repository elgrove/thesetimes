from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .models import ArticleSchema

router = APIRouter()


@router.post("/", response_description="Add new article")
async def create_task(request: Request, article: ArticleSchema = Body(...)):
    article = jsonable_encoder(article)
    new_article = await request.app.mongodb["articles"].insert_one(article)
    created_article = await request.app.mongodb["articles"].find_one(
        {"_id": str(new_article.inserted_id)}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED)


@router.get("/", response_description="List all articles")
async def list_articles(request: Request):
    articles = []
    for a in await request.app.mongodb["articles"].find().to_list(length=250):
        articles.append(a)
    return articles


@router.get("/{id}", response_description="Get a single article")
async def show_article(id: str, request: Request):
    if (
        article := await request.app.mongodb["articles"].find_one({"_id": id})
    ) is not None:
        return article

    raise HTTPException(status_code=404, detail=f"Article {id} not found")
