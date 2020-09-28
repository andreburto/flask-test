#!/usr/bin/env bash

$(aws ecr get-login --registry-ids 441882069681 --no-include-email)

docker build --tag flask-test:latest .

docker tag flask-test:latest 441882069681.dkr.ecr.us-east-1.amazonaws.com/flask-test:latest

docker push 441882069681.dkr.ecr.us-east-1.amazonaws.com/flask-test:latest
