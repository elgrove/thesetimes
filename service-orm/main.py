from thesetimes_orm.database import database_setup, run_migrations, migration_required

if __name__ == "__main__":
    database_setup()
    if migration_required():
        run_migrations()
