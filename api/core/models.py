from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId


class ArticleSchema(BaseModel):
    source: str = Field(...)
    source_short: str = Field(...)
    pagerank: int = Field(...)
    url: str = Field(...)
    category: str = Field(...)
    title: str = Field(...)
    author: str = Field(...)
    pubdate: datetime = Field(...)
    body: list = Field(...)

    class Config:
        {
            "example": {
                "source": "BBC News",
                "source_short": "bbc",
                'pagerank': '1',
                "url": "https://www.bbc.co.uk/news/world-59109186",
                "category": "News",
                "title": "Man Bites Dog",
                "author": "John Smith",
                "pubdate": "2021-01-01T00:00:00.000Z",
                "body": ["A man bit a dog today.", "Further news to follow"],
            }
        }
