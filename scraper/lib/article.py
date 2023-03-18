from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects import postgresql

from lib.database import get_db_engine

Base = automap_base()

engine = get_db_engine()
Base.prepare(engine, reflect=True)

Article = Base.classes.articles
