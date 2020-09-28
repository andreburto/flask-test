#!/usr/bin/env bash

DIR_PATH="$(dirname $0)"

aws cloudformation delete-stack --stack-name "flask-test-01"

aws cloudformation wait stack-delete-complete --stack-name "flask-test-01"

aws cloudformation create-stack --stack-name "flask-test-01" \
--template-body "file://${DIR_PATH}/template-01.yml" \
--parameters "file://${DIR_PATH}/template-01.json" \
--capabilities CAPABILITY_IAM

aws cloudformation wait stack-create-complete --stack-name "flask-test-01"
