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

@dataclass
Article
.headline
.body
.authors
.pubdate
.etc...

@dataclass
Publication
.homepage
.article_root
.

PublicationScraper(Publication)
.article_links
.scrape_headline()
.scrape_body()
.scrape_metadata()

ScraperDirector(PublicationScraper)

-----

database container starts
orm container starts and runs and exits
scraper container starts
