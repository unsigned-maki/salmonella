# Salmonella

School project for Project Management class which is supposed to become an online poll website similar to [StrawPoll](https://www.strawpoll.me/).

# Setup

- [Download](https://www.python.org/downloads/release/python-3912/) and install Python 3.9 or higher
- Make sure Python was added to your PATH
- Run `pip install pipenv`
- Clone the repository using `git clone https://github.com/unsigned-maki/salmonella`
- Install the [MongoDB Community Server](https://www.mongodb.com/try/download/community) or use the [docker-compose.yml](https://github.com/unsigned-maki/salmonella/blob/master/mongodb/docker-compose.yml) provided
- Run `pipenv install` within the `salmonella` directory
- A new virtualenv with the required modules should be created for you
- Run `pipenv run flask run` within the `salmonella` directory
- The server should now be running on port 5000

# Libraries

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Halfmoon CSS](https://www.gethalfmoon.com/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
- [MongoEngine](http://mongoengine.org)
- [Chart.js](https://www.chartjs.org)
- [Toastr](https://github.com/CodeSeven/toastr)
