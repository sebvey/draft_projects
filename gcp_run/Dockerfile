FROM python:3.8.12-buster

COPY requirements.txt requirements.txt
COPY base_prj base_prj

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn base_prj.api.api:app --host 0.0.0.0 --port $PORT
