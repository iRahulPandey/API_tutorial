from fastapi import FastAPI, Query # from fast API
import uvicorn
import joblib 
import pandas as pd
from pydantic import BaseModel

# import model
bm = joblib.load("boston_model.joblib")

# create app
app = FastAPI()

# create dict
class Modeldict(BaseModel):
  LSTAT: float
  INDUS: float
  NOX: float
  PTRATIO: float
  RM: float
  TAX: float
  DIS: float
  AGE: float

@app.get('/')
async def index():
  return {"text":"Our First route"}

@app.post('/predict')
def predict_species(inputdict: Modeldict):
    data = inputdict.dict()
    query = pd.DataFrame()
    query = query.append(data, ignore_index=True)
    prediction = list(bm.predict(query))
    print(prediction)
    return {
        'prediction': prediction
    }

#if __name__ == '__main__':
  #uvicorn.run(app, host='0.0.0.0', port=9696)
