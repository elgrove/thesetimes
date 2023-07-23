Website service - flask
API service - fastapi or django-ninja
ORM service - sqlalchemy
Scraper service - selenium/bs4
Database - postgres

GA builds the docker containers and publishes them
Linode cron or watchtower to keep the containers updated

github actions
on merge into main:
    - semantic release
    - build  containers



ROADMAP
- [x] scheduling for scraper
- [x] homepage ranking
- [x] latest news page (as opposed to ranked)
- [ ] deal with articles updating
  - [ ] query db for article url. if not found, insert
  - [ ] if found, compare hash of the title+body to the db
  - [ ] update the existing row if hash != 
  - [ ] add 
- [ ] cicd publishes docker containers on merge into main
- [ ] scrape images and charts
- [x] add publication-specific pages
- [ ] add category to database and add category pages
- [/] add publications
  - [x] new yorker
  - [x] nyt
  - [x] economist
  - [ ] bbc
  - [ ] athletic (possibly a different service)
- [ ] reverse proxy
- [/] tests for flask app
