from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)  # TODO UUID
    publication_name = Column(String, nullable=False)
    publication_short = Column(String(6), nullable=False)
    published_date = Column(DateTime, nullable=False)
    url = Column(String, nullable=False)
    authors = Column(String, nullable=False)
    title = Column(String, nullable=False)
    body = Column(postgresql.ARRAY(String, dimensions=1), nullable=False)

    def __repr__(self):
        return f"{self.publication_name} - {self.title}"
