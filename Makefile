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