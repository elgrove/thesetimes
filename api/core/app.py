from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Root"])
async def get_root():
    return {'message': "This is API Root, use /news for articles"}
