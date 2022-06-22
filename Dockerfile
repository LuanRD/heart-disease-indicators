FROM python:3.9-slim

COPY ./requirements-2.txt /usr/requirements.txt

WORKDIR /usr

RUN pip3 install -r requirements.txt

COPY ./src /usr/src
COPY ./models /usr/models

ENTRYPOINT [ "python3"]

CMD [ "src/app/api_docker.py" ]