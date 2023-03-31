clean:
	rm -rf orm/lib/alembic/versions/*
	sudo rm -rf database
	mkdir database
	sudo chown -R 999:999 ./database

prepare:
	cd orm && poetry export -f requirements.txt --without-hashes --without-urls --output requirements.txt
	cd web && poetry export -f requirements.txt --without-hashes --without-urls --output requirements.txt
	cd scraper && poetry export -f requirements.txt --without-hashes --without-urls --output requirements.txt

up: prepare
	sudo docker compose up --build

upd: prepare
	sudo docker compose up -d --build

webapp-macos:
	cd web && DATABASE_USER=articles_user DATABASE_SERVICE=100.93.30.84 POSTGRES_PORT=5432 DATABASE_NAME=thesetimes POSTGRES_PASSWORD=1111 poetry run python main.py