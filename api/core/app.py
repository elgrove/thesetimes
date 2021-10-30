from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from bson import ObjectId

from .routes import router as api_router
from .routes import templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router, tags=["articles"], prefix="/api")


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
