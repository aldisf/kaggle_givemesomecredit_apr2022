from fastapi import APIRouter

from src.formatters.requests import DelinquencyReq
from src.formatters.responses import DelinquencyResp
from src.services import predict_delinquency

router = APIRouter(prefix="/delinquency", tags=["delinquency"])

# Get predicted delinquency probability
@router.post("/delinquency", response_model=DelinquencyResp)
def get_delinquency_probability(request: DelinquencyReq):

    proba = predict_delinquency.predict_delinquency_proba(request)
    resp = DelinquencyResp(DefaultProb=proba, metadata=request)

    return resp
