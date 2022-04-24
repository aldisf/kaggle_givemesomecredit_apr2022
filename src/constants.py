import os

TRAIN_DATA_PATH = "data/cs-training.csv"
TEST_DATA_PATH = "data/cs-test.csv"
SUBMISSIONS_FOLDER_PATH = "submissions"

LABEL_COL = "SeriousDlqin2yrs"

FEATURES_COL_LIST = [
    "RevolvingUtilizationOfUnsecuredLines",
    "age",
    "NumberOfTime30-59DaysPastDueNotWorse",
    "DebtRatio",
    "MonthlyIncome",
    "NumberOfOpenCreditLinesAndLoans",
    "NumberOfTimes90DaysLate",
    "NumberRealEstateLoansOrLines",
    "NumberOfTime60-89DaysPastDueNotWorse",
    "NumberOfDependents",
]

RANDOM_SEED = 20220423
VAL_SIZE = 0.1

TRAIN_ARTIFACTS_FOLDER_PATH = "src/train_artifacts"
TRAINED_IMPUTER_PATH = os.path.join(TRAIN_ARTIFACTS_FOLDER_PATH, "imputer.joblib")
CAP_DICT_PATH = os.path.join(TRAIN_ARTIFACTS_FOLDER_PATH, "capdict.joblib")
TRAINED_LGBM_MODEL_PATH = os.path.join(TRAIN_ARTIFACTS_FOLDER_PATH, "tuned_lgbm.joblib")
