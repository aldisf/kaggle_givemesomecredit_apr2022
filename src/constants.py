TRAIN_DATA_PATH = "data/cs-training.csv"
TEST_DATA_PATH = "data/cs-test.csv"

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
VAL_SIZE = 0.2
