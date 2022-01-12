# pylint: disable=missing-module-docstring, line-too-long
#!/usr/bin/python3
import pickle
from pydantic.main import BaseModel
import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd

from database import engine
import models


# Instantiate API
app = FastAPI(title='Bank Statement Clearing API')

# Create database connection
models.Base.metadata.create_all(bind=engine)

# Import model outside the predict function to avoid latency
rf_model = pickle.load(open('model.pickle', 'rb'))

# Create a data object
class BscData(BaseModel):
    f_iban_history_available:float
    f_iban_history_match:float
    f_customer_iban_available:float
    f_pair_ibans_matches:float
    f_pair_amounts_equals:float
    f_pair_invoiceId_in_reftext_leven:float
    f_pair_ex_invoiceId_in_reftext_leven:float
    f_reftext_op_bez_fuzzy_wuzzy:float
    f_bsi_name_op_bez_fuzzy_wuzzy:float
    f_customer_group_amount_match:float



@app.get('/')
def home_func() -> dict:
    '''Homepage function. Return value could be replaced with an html file
    if front-end is required for this server.
    '''
    return {'value': 'API is working as expected.'}

@app.post('/predict')
def predict(data:BscData):
    # Convert BscData to numpy array and reshape
    X = np.array(list(data.dict().values())).reshape(-1,10)

    # Predict
    prediction = rf_model.predict(X)

    # Returning prediction as int(0 or 1), it can be str too.
    # In that case it will return ['false'] or ['true']
    return int(prediction)


if __name__ == "__main__":
    # Changed it from app to 'main:app' to reload changes automatically.
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
