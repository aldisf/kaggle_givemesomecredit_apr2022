# kaggle_givemesomecredit_apr2022

This assignment is based on the Kaggle competition [GiveMeSomeCredit](https://www.kaggle.com/competitions/GiveMeSomeCredit).
Data and descriptions can be found in the link above.

Analysis, modeling and answers to questions can be found the notebook file [analysis_and_modeling.ipynb](./analysis_and_modeling.ipynb)

```sh
curl -X 'POST' \
  'http://127.0.0.1:8888/delinquency/delinquency' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "RevolvingUtilizationOfUnsecuredLines": 0.88551908,
  "age": 43,
  "NumberOfTime30_59DaysPastDueNotWorse": 0,
  "DebtRatio": 0.177512717,
  "MonthlyIncome": 5700,
  "NumberOfOpenCreditLinesAndLoans": 4,
  "NumberOfTimes90DaysLate": 0,
  "NumberRealEstateLoansOrLines": 0,
  "NumberOfTime60_89DaysPastDueNotWorse": 0,
  "NumberOfDependents": 0
}'
```
