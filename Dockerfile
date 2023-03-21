FROM python:3.11-alpine

WORKDIR /flaskAPI-docker

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "run.py"]


