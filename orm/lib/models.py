from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects import postgresql

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    publication = Column(String)
    pubdate = Column(DateTime)
    authors = Column(String)
    title = Column(String)
    body = Column(postgresql.ARRAY(String, dimensions=1))

    def __repr__(self):
        return f"{self.publication} - {self.title}"
