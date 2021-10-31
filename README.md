# These Times

A news aggregator that pulls and presents articles from various sources, including those behind a paywall.

### Built with

- Python
- FastAPI, Jinja2, Motor
- MongoDB
- BeautifulSoup, Selenium
- Docker, docker-compose

Enormous props to github.com/iamadamdev for their invaluable bypass-paywalls browser extension, without which this would not be possible.

## Getting Started

### Installing

* Clone this repository
* `cd` into the repository directory and run `docker-compose up -d`
* The web server will listen on port 8558
* The scraper will run every day at the 07, 12, 16 and 19 hour

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
