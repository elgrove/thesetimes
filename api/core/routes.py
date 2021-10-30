from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from bson import ObjectId

from .models import ArticleSchema
from .app import app
from .utils import print_date, parse_json

router = APIRouter()
templates = Jinja2Templates(directory="templates")
templates.env.filters["print_date"] = print_date
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router, tags=["articles"], prefix="/api")


##### HTML TEMPLATE ROUTES


@app.get("/", tags=["Home"], response_class=HTMLResponse)
async def get_homepage(request: Request):
    articles = []
    for a in (
        await request.app.mongodb["articles"]
        .find()
        .sort("pubdate", -1)
        .to_list(length=60)
    ):
        articles.append(a)
    # random.shuffle(articles)
    return templates.TemplateResponse(
        "home.html", {"request": request, "articles": articles}
    )


@app.get("/article/{id}", tags=["Article"], response_class=HTMLResponse)
async def get_article(id: str, request: Request):
    if (
        article := await request.app.mongodb["articles"].find_one({"_id": ObjectId(id)})
    ) is not None:
        return templates.TemplateResponse(
            "article.html", {"request": request, "a": article}
        )

    raise HTTPException(status_code=404, detail=f"Article {id} not found")


##### JSON API ROUTES


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
    for a in (
        await request.app.mongodb["articles"].find().sort("_id", -1).to_list(length=60)
    ):
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
