import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from core.app import app
from core.routes import router as news_router


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient("mongodb://localhost:27017")
    app.mongodb = app.mongodb_client["grovetimes"]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(news_router, tags=["articles"], prefix="/news")

if __name__ == "__main__":
    uvicorn.run("core.app:app", host="0.0.0.0", port=8558, reload=True)
