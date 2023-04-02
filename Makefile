clean:
	rm -rf orm/core/alembic/versions/*
	sudo rm -rf database
	mkdir database
	sudo chown -R 999:999 ./database

up:
	sudo docker compose up --build

upd:
	sudo docker compose up -d --build

localweb:
	cd web && DATABASE_USER=articles_user DATABASE_SERVICE=100.93.30.84 POSTGRES_PORT=5432 DATABASE_NAME=thesetimes POSTGRES_PASSWORD=1111 poetry run python main.py

development: clean upd localweb