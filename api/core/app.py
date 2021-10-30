from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from core.routes import router as news_router
from core.routes import parse_json
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
from bson import json_util, ObjectId


app = FastAPI()

app.include_router(news_router, tags=["articles"], prefix="/api")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", tags=["Home"], response_class=HTMLResponse)
async def get_homepage(request: Request):
    articles = []
    for a in (
        await request.app.mongodb["articles"].find().sort("_id", -1).to_list(length=60)
    ):
        articles.append(parse_json(a))
    return templates.TemplateResponse(
        "home.html", {"request": request, "articles": articles}
    )


# @app.get("/{id}", tags=["Article"], response_class=HTMLResponse)
# async def get_article(id: str, request: Request):
#     if (
#         article := await request.app.mongodb["articles"].find_one({"_id": ObjectId(id)})
#     ) is not None:
#         return templates.TemplateResponse(
#             "article.html", {"request": request, "a": article}
#         )

#     raise HTTPException(status_code=404, detail=f"Article {id} not found")
