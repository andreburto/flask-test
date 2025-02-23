# flask-test

## About

This is a project that works with Flask, Docker, and Amazon AWS. 
It sets up a small server for testing HTTP requests within an ECS environment.
The core of this project is testing out ECS and creating a basic template to use in other projects.

## Setup

### Local

1. Install Docker and Python3.
2. Change to the top level directory of the project. 
3. Run `python -m pip install -r requirements.txt`, after creating a venv if desired.
4. Use `docker build -t flask-test .` to build the Docker image.
5. Run `docker run -p 8000:8000 flask-test` to start the server.
6. From another terminal, use the `client.py` script to test the server.

### AWS

TBD

## To Do

1. Setup [Cypress](https://www.cypress.io/) tests to be used as post-deployment tests.
2. Add instructions for setting up the AWS environment.
3. Translate `template_setup.sh` and `push.sh` scripts into [TerraForm](https://www.terraform.io/).
