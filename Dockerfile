FROM python:3.11-alpine

WORKDIR /flaskAPI-docker

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "run.py"]


