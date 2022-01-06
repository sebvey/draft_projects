from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()

@app.get('/')
def index():

    return {"ok":True}

@app.get("/predict")
def predict(str_date):


    try :
        date_to_predict = datetime.strptime(str_date,"%Y-%m-%d")

    except ValueError :
        return { 'ko':'date format invalid'}

    return { 'prediction':date_to_predict + timedelta(1) }

