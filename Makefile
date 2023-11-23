clean:
	rm -rf service-orm/alembic/versions/*
	sudo rm -rf service-database
	mkdir service-database
	sudo chown -R 999:999 ./service-database
	rm -rf package-orm/dist/*

upd: clean build
	sudo docker compose up -d

deploy: clean install build
	sudo docker compose up -d

develop: clean install build
	sudo docker compose up

SERVICES := service-orm service-scraper service-web
PACKAGES := package-orm

build:
	$(foreach service,$(SERVICES),sudo docker build -f $(service)/Dockerfile -t $(service):latest .;)

test:
	$(foreach service,$(SERVICES),cd $(service) && make test && cd ..;)
	$(foreach package,$(PACKAGES),cd $(package) && make test && cd ..;)

lint:
	$(foreach service,$(SERVICES),cd $(service) && make lint && cd ..;)
	$(foreach package,$(PACKAGES),cd $(package) && make lint && cd ..;)

lock:
	$(foreach service,$(SERVICES),cd $(service) && poetry lock && cd ..;)
	$(foreach package,$(PACKAGES),cd $(package) && poetry lock && cd ..;)

install:
	$(foreach service,$(SERVICES),cd $(service) && poetry install && cd ..;)
	$(foreach package,$(PACKAGES),cd $(package) && poetry install && cd ..;)

venv:
	$(foreach service,$(SERVICES),cd $(service) && rm poetry.lock; rm -rf .venv; poetry install; cd ..;)
	$(foreach package,$(PACKAGES),cd $(package) && rm poetry.lock; rm -rf .venv; poetry install; cd ..;)

