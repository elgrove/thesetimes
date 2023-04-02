import os

from alembic import command
from alembic.config import Config
import sqlalchemy
from sqlalchemy_utils import create_database, database_exists


def get_maintenance_db_engine():
    """Create a database engine to the default db 'postgres' to facilitate maintenance operations."""
    connection_url = sqlalchemy.engine.URL.create(
        "postgresql+psycopg2",
        username=os.environ["POSTGRES_USER"],
        host=f"{os.environ['DATABASE_SERVICE']}",
        port=int(os.environ["POSTGRES_PORT"]),
        database="postgres",
        password=os.environ["POSTGRES_PASSWORD"],
    )

    return sqlalchemy.create_engine(
        connection_url, connect_args={"sslmode": "disable"}, echo=False
    )


def get_admin_db_engine():
    """Create a database engine to the our db 'thesetimes' to execute setup operations."""
    connection_url = sqlalchemy.engine.URL.create(
        "postgresql+psycopg2",
        username=os.environ["DATABASE_ADMIN"],
        host=f"{os.environ['DATABASE_SERVICE']}",
        port=int(os.environ["POSTGRES_PORT"]),
        database=os.environ["DATABASE_NAME"],
        password=os.environ["POSTGRES_PASSWORD"],
    )

    return sqlalchemy.create_engine(
        connection_url, connect_args={"sslmode": "disable"}, echo=False
    )


def run_migrations():
    """Run Alembic migrations, autogenerating versions as needed."""
    alembic_cfg = Config("alembic.ini")
    command.revision(alembic_cfg, autogenerate=True, message="Autogenerated")
    command.upgrade(alembic_cfg, "head")


def user_exists(user, conn):
    """Check if user already exists in the database."""
    result = conn.execute(
        f"SELECT usename from pg_catalog.pg_user WHERE usename = '{user}';"
    )
    if not result.first():
        return False
    return True


def database_setup():
    """Execute a sequence of SQL commands to set up the database."""
    maintenance_engine = get_maintenance_db_engine()
    with maintenance_engine.connect() as conn:
        for user in [os.environ["DATABASE_ADMIN"], os.environ["DATABASE_USER"]]:
            if not user_exists(user, conn):
                conn.execute(
                    f"CREATE USER {user} WITH ENCRYPTED PASSWORD '{os.environ['POSTGRES_PASSWORD']}';"
                )

        conn.execute(f"ALTER ROLE {os.environ['DATABASE_ADMIN']} CREATEDB CREATEROLE;")

    admin_engine = get_admin_db_engine()
    if not database_exists(admin_engine.url):
        create_database(admin_engine.url)

    with admin_engine.connect() as conn:
        conn.execute('CREATE EXTENSION IF NOT EXISTS "pgcrypto";')
        # grant privileges on existing tables
        conn.execute(
            f"GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO {os.environ['DATABASE_ADMIN']};"
        )
        conn.execute(
            f"GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO {os.environ['DATABASE_ADMIN']};"
        )
        conn.execute(
            f"GRANT SELECT,UPDATE,INSERT,DELETE ON ALL TABLES IN SCHEMA public TO {os.environ['DATABASE_USER']};"
        )
        conn.execute(
            f"GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO {os.environ['DATABASE_USER']};"
        )

        # grant privileges on future tables
        conn.execute(
            f"""ALTER DEFAULT PRIVILEGES FOR ROLE {os.environ['DATABASE_ADMIN']} IN SCHEMA public
                GRANT SELECT,UPDATE,INSERT,DELETE ON TABLES TO {os.environ['DATABASE_USER']};"""
        )
        conn.execute(
            f"""ALTER DEFAULT PRIVILEGES FOR ROLE {os.environ['DATABASE_ADMIN']} IN SCHEMA public
                GRANT ALL PRIVILEGES ON SEQUENCES TO {os.environ['DATABASE_USER']};"""
        )
