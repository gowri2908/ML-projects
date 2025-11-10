from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load saved preprocessor and model
preprocessor = joblib.load('preprocessor.pkl')
model = joblib.load('xgb_credit_risk_model.pkl')

# Define input features expected by the API (match your training dataset columns exactly)
class CreditRiskInput(BaseModel):
    Age: int
    Sex: str
    Job: int
    Housing: str
    Saving_accounts: str
    Checking_account: str
    Credit_amount: int
    Duration: int
    Purpose: str
  

@app.post("/predict")
def predict(data: CreditRiskInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.model_dump()])


    # Preprocess input features
    transformed = preprocessor.transform(input_df)

    # Predict credit risk class
    prediction = model.predict(transformed)

    # Convert prediction to string label if needed
    prediction_label = prediction[0]

    return {"prediction": prediction_label}
