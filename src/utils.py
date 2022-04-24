import os
import pandas as pd
import numpy as np

from src.constants import SUBMISSIONS_FOLDER_PATH
from typing import Union


def read_givemesomecredit_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path).rename(columns={"Unnamed: 0": "id"})


def create_submission_data(
    test_id: pd.DataFrame,
    test_proba: Union[pd.Series, np.ndarray],
    submission_name: str,
) -> pd.DataFrame:

    test_id["Probability"] = test_proba
    outfilepath = os.path.join(SUBMISSIONS_FOLDER_PATH, submission_name)
    test_id.to_csv(outfilepath, index=False)
