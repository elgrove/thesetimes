Website service - flask
API service - fastapi or django-ninja
ORM service - sqlalchemy
Scraper service - selenium/bs4
Database - postgres


CICD
Nox, linting, testing

What would a CICD process do?
Lint, test
rebuild docker containers where needed
docker compose up

where am i going to deploy? linode
how am i  going to do github actions? ssh into linode

github actions:

on pr:
    - lint
    - test

on merge into main:
    - ssh into linode with key auth
    - git pull
    - dcp up --build


Public/private attributes

Todo

before mvp
- log main and m1 into alvgrv github
- lint? ruff?
- tests on flask app
- scheduling on scraper
- can i develop the flask app inside the container?
- reverse proxy maybe traefik or caddy


after mvp:
- deal with articles updating
- push to github
- cicd based on pushes to github (after mvp)
- lint
- images and charts
- homepage ranking
- latest news page sorted by pubdate
- other publications - nyt, econ, bbc, athletic, new yorker, ft opinion, ft life and arts
- 