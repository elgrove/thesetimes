from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json
from bson import json_util, ObjectId
from .models import ArticleSchema


router = APIRouter()


def parse_json(data):
    return json.loads(json_util.dumps(data))


@router.post("/", response_description="Add new article")
async def create_article(request: Request, article: ArticleSchema = Body(...)):
    article = jsonable_encoder(article)
    new_article = await request.app.mongodb["articles"].insert_one(article)
    created_article = await request.app.mongodb["articles"].find_one(
        {"_id": ObjectId(new_article.inserted_id)}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED)


@router.get("/", response_description="List all articles")
async def list_articles(request: Request):
    articles = []
    for a in await request.app.mongodb["articles"].find().to_list(length=250):
        articles.append(parse_json(a))
    return articles


@router.get("/{id}", response_description="Get a single article")
async def show_article(id: str, request: Request):
    if (
        article := await request.app.mongodb["articles"].find_one({"_id": ObjectId(id)})
    ) is not None:
        return parse_json(article)

    raise HTTPException(status_code=404, detail=f"Article {id} not found")


@router.get("/find/", response_description="Get a single article by title")
async def show_article(title: str, request: Request):
    if (
        article := await request.app.mongodb["articles"].find_one({"title": title})
    ) is not None:
        return parse_json(article)

    raise HTTPException(status_code=404, detail=f"Article {id} not found")
