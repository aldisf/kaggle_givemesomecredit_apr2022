import joblib
import pandas as pd
from src.preprocessing.preprocessing_functions import get_capped_df
from src.formatters.requests import DelinquencyReq
from src.constants import (
    TRAINED_IMPUTER_PATH,
    CAP_DICT_PATH,
    TRAINED_LGBM_MODEL_PATH,
    FEATURES_COL_LIST,
    LABEL_COL,
)

IMPUTER = joblib.load(TRAINED_IMPUTER_PATH)
CAP_DICT = joblib.load(CAP_DICT_PATH)
MODEL = joblib.load(TRAINED_LGBM_MODEL_PATH)


def predict_delinquency_proba(
    request: DelinquencyReq,
    imputer=IMPUTER,
    cap_dict=CAP_DICT,
    model=MODEL,
) -> float:

    req_data = pd.DataFrame(
        {ft: [request.dict().get(ft.replace("-", "_"))] for ft in FEATURES_COL_LIST}
    )

    # Filler to adhere to imputer
    req_data["id"] = -1
    req_data[LABEL_COL] = -1

    req_data = pd.DataFrame(
        columns=req_data.columns,
        data=imputer.transform(req_data),
    )

    req_data = get_capped_df(
        df=req_data,
        cap_dict=cap_dict,
    )

    delinquency_proba = model.predict_proba(req_data[FEATURES_COL_LIST])[0][1]

    return delinquency_proba
