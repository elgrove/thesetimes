from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from bson import ObjectId

from .router import router as api_router
from .router import templates
from .utils import pub_dict  # short name to long name converter

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router, tags=["articles"], prefix="/api")


@app.get("/", response_class=HTMLResponse)
async def get_homepage(request: Request):
    articles = []
    for a in (
        await request.app.mongodb["articles"]
        .find()
        .sort("pubdate", -1)
        .to_list(length=100)
    ):
        articles.append(a)

    return templates.TemplateResponse(
        "home.html", {"request": request, "articles": articles}
    )


@app.get("/pubs/", response_class=HTMLResponse)
async def get_pubs_list(request: Request):
    pubs = []
    for a in await request.app.mongodb["articles"].find().to_list(100):
        pubs.append(a["source"])
    pubs = list(dict.fromkeys(pubs))
    # convert long to short for url values
    pub_dict_inverse = {v: k for k, v in pub_dict.items()}
    pubs_short = [pub_dict_inverse[n] for n in pubs]

    return templates.TemplateResponse(
        "pubs.html",
        {"request": request, "pubs": pubs, "pub_dict_inverse": pub_dict_inverse},
    )


@app.get("/pubs/{pub}", response_class=HTMLResponse)
async def get_pub_home(pub: str, request: Request):
    this_pub = pub_dict[pub]  # convert short to long for db find
    articles = []
    for a in (
        await request.app.mongodb["articles"]
        .find({"source": this_pub})
        .sort("pubdate", -1)
        .to_list(length=100)
    ):
        articles.append(a)

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
