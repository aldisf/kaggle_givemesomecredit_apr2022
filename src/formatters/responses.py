from pydantic import BaseModel
from src.formatters.requests import DelinquencyReq


class DelinquencyResp(BaseModel):
    DefaultProb: float
    metadata: DelinquencyReq
