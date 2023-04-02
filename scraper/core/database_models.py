from sqlalchemy.ext.automap import automap_base

from core.database import get_db_engine

Base = automap_base()

engine = get_db_engine()

Base.prepare(engine, reflect=True)

Article = Base.classes.articles
