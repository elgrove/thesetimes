SERVERLESS

Database setup & migrations:
pass

Ticker:
Scheduled
Loop through list of sites to scrape
Publishes event for site scraper

Site scraper:
pass

Article scraper:
pass


SERVERFUL


Website service - flask
API service - fastapi or django-ninja
ORM service - sqlalchemy
Scraper service - selenium/bs4
Database - postgres

CICD
Nox, linting, testing

What would a CICD process do?
Lint, test
Deploy database container
Run db setup/migrate function
Deploy service containers