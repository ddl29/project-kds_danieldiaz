
# Production Engineering - Week 1 - Portfolio Site
#Using Docker containers!
## Gorilla Gang Portfolio Site

Team members Daniel Diaz, Kaitlyn Chau, and Set Lynn created a portfolio website that feature different personalities.


## Inspiration
We wanted to have a single place where we could put any teammates we are working with on a common project, so it can be a reference website of the creators behind that project!

## What it does
It is a single website where we can explore all of a project's developers portfolios.

## How we built it
Using Flask and Jinja for the server, routing and templates reutilization and the web development common parts: HTML, Javascript and CSS.

## Challenges we ran into
Designing a first mock.
Defining the scope.
Working as a team.
We were new to Flask and Jinja.

## Accomplishments that we're proud of
-Familiarize with basic Flask rapidly.
-Using Jinja template for NavBar.
-Using Google Maps API.
-Extra work: second website tab (Set's effort).
-Slideshow on Hobbies section.

## What we learned
-Basic Flask and Jinja.
-Set up a virtual environment in Python.
-Git flow control: creating branches and doing pull requests.

## What's next for Gorilla Gang Portfolios
-Implement Jinja templates for "Education", "Experience" and "Hobbies" sections.
-Use the Jinja templates and replicate another website (Daniel's).


## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser!
