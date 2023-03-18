import os

import sqlalchemy


def get_db_engine():
    connection_url = sqlalchemy.engine.URL.create(
        "postgresql+psycopg2",
        username=os.environ["DATABASE_USER"],
        host=f"{os.environ['DATABASE_SERVICE']}",
        port=int(os.environ["POSTGRES_PORT"]),
        database=os.environ["DATABASE_NAME"],
        password=os.environ["POSTGRES_PASSWORD"],
    )

    return sqlalchemy.create_engine(
        connection_url,
        connect_args={"sslmode": "disable"},
        echo=False,
    )
