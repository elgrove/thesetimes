from sqlalchemy.ext.automap import automap_base

from core.engine import get_engine

Base = automap_base()

engine = get_engine()

Base.prepare(engine, reflect=True)

Article = Base.classes.articles
