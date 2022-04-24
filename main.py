from fastapi import FastAPI
from src.routes import delinquency


app = FastAPI(title="Delinquency Prediction API")
app.include_router(delinquency.router)


@app.get("/")
def home():
    return "Delinquency Prediction API! please visit /docs endpoint for details"