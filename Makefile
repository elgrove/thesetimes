build-clean:
	rm -rf orm/lib/alembic/versions/*
	sudo rm -rf database
	mkdir database
	sudo chown -R 999:999 ./database
	sudo docker compose up --build