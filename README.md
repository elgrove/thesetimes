# These Times

A news aggregator and reader that pulls and presents articles from various sources, including those behind a paywall. As with all good software, it was made to solve a problem in my own life.

Currently serving:  
News: FT, NYT, WSJ, BBC, DW  
Opinion/Features: The Economist, The New Yorker  
Sports: Sky Sports, Football365  
Tech: Ars Technica, MIT Technology Review  

With plans to add more, especially in opinion, tech and sports as these categories are quite bare at the moment.

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
* The scraper will run through the day at regular intervals to ensure freshness

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
