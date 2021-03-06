from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from bson import ObjectId
from datetime import datetime as dt

from .router import router as api_router
from .router import templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router, tags=["articles"], prefix="/api")


@app.get("/", response_class=HTMLResponse)
async def get_homepage(request: Request):
    articles = []
    for a in (
        await request.app.mongodb["articles"]
        .find(
            {"category": "News", "source_short": {"$in": ["nyt", "wsj", "ft", "bbc"]}}
        )
        .sort("_id", -1)  # newest-scraped articles
        .to_list(length=60)
    ):
        articles.append(a)

    articles = sorted(
        articles,
        key=lambda d: (
            dt.strptime(d["pubdate"], "%Y-%m-%dT%H:%M:%S").date(),
            1 / d["pagerank"],
        ),
        reverse=True,
    )

    return templates.TemplateResponse(
        "home.html", {"request": request, "articles": articles}
    )


# async def get_landing(request: Request):
#     articles = []
#     for a in (
#         await request.app.mongodb["articles"]
#         .find()
#         .sort("pubdate", -1)
#         .to_list(length=40)
#     ):
#         articles.append(a)

#     return templates.TemplateResponse(
#         "home.html", {"request": request, "articles": articles}
#     )


@app.get("/latest", response_class=HTMLResponse)
async def get_homepage(request: Request):
    articles = []
    for a in (
        await request.app.mongodb["articles"]
        .find({"category": "News"})
        .sort("pubdate", -1)
        .to_list(length=100)
    ):
        articles.append(a)

    return templates.TemplateResponse(
        "home.html", {"request": request, "articles": articles}
    )


@app.get("/pubs/{pub}", response_class=HTMLResponse)
async def get_pub_home(pub: str, request: Request):
    articles = []
    for a in (
        await request.app.mongodb["articles"]
        .find({"source_short": pub})
        .sort("pagerank")
        .to_list(length=100)
    ):
        articles.append(a)

    articles = sorted(
        articles,
        key=lambda d: (
            dt.strptime(d["pubdate"], "%Y-%m-%dT%H:%M:%S").date(),
            1 / d["pagerank"],
        ),
        reverse=True,
    )

    return templates.TemplateResponse(
        "home.html", {"request": request, "articles": articles}
    )


@app.get("/article/{id}", response_class=HTMLResponse)
async def get_article(id: str, request: Request):
    if (
        article := await request.app.mongodb["articles"].find_one({"_id": ObjectId(id)})
    ) is not None:

        return templates.TemplateResponse(
            "article.html", {"request": request, "a": article}
        )

    raise HTTPException(status_code=404, detail=f"Article {id} not found")


@app.get("/{cat}", response_class=HTMLResponse)
async def get_pub_home(cat: str, request: Request):
    articles = []
    for a in (
        await request.app.mongodb["articles"]
        .find({"category": str.capitalize(cat)})
        .sort("pubdate", -1)
        .to_list(length=100)
    ):
        articles.append(a)

    articles = sorted(
        articles,
        key=lambda d: (
            dt.strptime(d["pubdate"], "%Y-%m-%dT%H:%M:%S").date(),
            1 / d["pagerank"],
        ),
        reverse=True,
    )

    return templates.TemplateResponse(
        "home.html", {"request": request, "articles": articles}
    )
