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
- [ ] cicd publishes docker containers on merge into main
- [ ] scrape images and charts
- [ ] add publication-specific pages
- [ ] add publications
  - [x] new yorker
  - [ ] nyt
  - [ ] economist
  - [ ] bbc
  - [ ] athletic
- [ ] reverse proxy
- [/] tests for flask app
