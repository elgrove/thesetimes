from lib.database import database_setup, run_migrations

if __name__ == "__main__":
    database_setup()
    run_migrations()
