FROM python:3.7-alpine

WORKDIR /app

COPY ./ /app

# Install any needed packages specified in requirements.txt
RUN apk update && \
    apk add --no-cache py3-setuptools python3-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "app.py"]
