# These Times

A news aggregator with articles from paywalled media sites, built as microservices orchestrated by docker compose.

The docker compose file contains five services, which come up in an order defined by the `depends_on` key in the config:

- a Postgres database
- an Alembic ORM service
- a Selenium webdriver server
- a home-rolled scraper service
- a Flask web server

## Quick start

- Clone this repo
- Run `make deploy`
- Hit the web server at `localhost:8000`

## Built with

- Docker, docker compose
- Selenium Grid
- [Bypass Paywalls](https://github.com/iamadamdev/bypass-paywalls-chrome) browser extension by iamadadev
- Postgres
- Python 3.9
- SQL Alchemy, Alembic
- Selenium, beautifulsoup4
- Flask, Jinja2, Gunicorn


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
