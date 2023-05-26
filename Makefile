clean:
	rm -rf service-orm/alembic/versions/*
	sudo rm -rf service-database
	mkdir service-database
	sudo chown -R 999:999 ./service-database
	rm -rf package-orm/dist/*

up: build
	sudo docker compose down
	sudo docker compose up

upd:
	sudo docker compose up -d --build

localweb:
	cd service-web && DATABASE_USER=articles_user DATABASE_SERVICE=100.93.30.84 POSTGRES_PORT=5432 DATABASE_NAME=thesetimes POSTGRES_PASSWORD=1111 poetry run python main.py

development: clean upd localweb

PACKAGES := package-orm
SERVICES := service-orm service-scraper service-web


build:
	$(foreach service,$(SERVICES),docker build -f $(service)/Dockerfile -t $(service):latest .;)

# test:
# 	$(foreach service,$(SERVICES),cd $(service) && poetry run pytest .;cd ..)
# 	$(foreach package,$(PACKAGES),cd $(package) && poetry run pytest .;cd ..)

format:
	$(foreach service,$(SERVICES),cd $(service) && poetry run black .; cd ..;)
	$(foreach package,$(PACKAGES),cd $(package) && poetry run black .; cd ..;)


lint:
	$(foreach service,$(SERVICES),cd $(service) && poetry run pylint --recursive=y .; cd ..;)
	$(foreach package,$(PACKAGES),cd $(package) && poetry run pylint --recursive=y .; cd ..;)

lock:
	$(foreach service,$(SERVICES),cd $(service) && poetry lock; cd ..;)
	$(foreach package,$(PACKAGES),cd $(package) && poetry lock; cd ..;)

install:
	$(foreach service,$(SERVICES),cd $(service) && poetry install; cd ..;)
	$(foreach package,$(PACKAGES),cd $(package) && poetry install; cd ..;)

