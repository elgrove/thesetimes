# These Times

A news aggregator with articles from paywalled media sites, self-hostable with docker-compose.

### Background

As with all good software, it was made to solve a problem in my own life.

This is deployed as a subdomain on my site but I won't share the address for obvious reasons. It's doing a great job so far, I'm enjoying having a one-stop shop for most of the sites I read for news.

I've tried to build it in a microservices-style architecture with REST API and HATEOAS. The API has GET, POST and DELETE endpoints and the scraper communicates with it in this way.

### Built with

- Python 3.8
- FastAPI + Jinja and Motor 
- MongoDB
- BeautifulSoup, Selenium
- Bootstrap 5
- Docker, docker-compose

### Credit

Enormous props to [github.com/iamadamdev]() for their invaluable bypass-paywalls browser extension, without which this would not be possible.

### Roadmap

- Secure the API with auth
- Use fuzzy matching to replace stories that are updated with new information as the story develops with the latest version
- Use fuzzy matching to group stories on the homepage into one item that are from different publications but about the same thing
- CI/CD
- Keep adding publications
- Add ability for user to select the publications they want to see

### Currently Serving

News:
- FT
- NYT
- WSJ
- BBC
- DW

Opinion/Features:
- The Economist
- The New Yorker  

Sports: 
- Sky Sports
- Football365  

Tech:
- Ars Technica
- MIT Technology Review  


### Installation

#### Prerequisites:
- Docker
- docker-compose
- That's it

#### Process:
* Clone this repository
* `cd` into the repository directory and run `docker-compose up -d`
* The web server will listen on port 8558
* The scraper will do a first run on startup and then run through the day at regular intervals

### License

This project is licensed under the MIT License - see the LICENSE.md file for details
