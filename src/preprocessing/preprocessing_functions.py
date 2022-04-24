import pandas as pd
import numpy as np
from typing import List

from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error


def get_cap_dict(
    train_df: pd.DataFrame,
    ratio_cols: List[str],
    non_ratio_cols: List[str],
    percentile_for_cap: float = 99.0,
) -> dict:
    cap_dict = {}

    for col in ratio_cols:
        cap_dict[col] = 1.0

    for col in non_ratio_cols:
        cap = np.nanpercentile(train_df[col], percentile_for_cap)
        cap_dict[col] = cap

    return cap_dict


def get_capped_df(
    df: pd.DataFrame,
    cap_dict: dict,
) -> pd.DataFrame:
    capped_df = df.copy(deep=True)

    for col, cap in cap_dict.items():
        capped_df[col] = np.where(capped_df[col] > cap, cap, capped_df[col])

    return capped_df


def get_imputer_and_imputed_df_simple(
    impute_strategy: str,
    original_df: pd.DataFrame,
    label_col: str,
):
    assert impute_strategy in (
        "mean",
        "most_frequent",
        "median",
    ), "impute_strategy must be one of 'mean', 'most_frequent', or 'median'"

    imputer = SimpleImputer(strategy=impute_strategy)
    imputer.fit(original_df.dropna(subset=[label_col]))

    imputed_df = pd.DataFrame(
        columns=original_df.columns, data=imputer.transform(original_df)
    )

    return imputer, imputed_df


def get_imputer_and_imputed_df_regressor(
    regressor_class,
    regressor_kwargs: dict,
    cols_to_impute_via_regression: List[str],
    cols_dtype: List,
    original_df: pd.DataFrame,
    feature_cols_list: List[str],
):

    imputer_dict = {}

    imputed_df = original_df.copy(deep=True)

    for idx, col in enumerate(cols_to_impute_via_regression):

        regressor = regressor_class(**regressor_kwargs)

        regressor_impute_train_df = original_df.copy(deep=True)
        regressor_impute_train_df = regressor_impute_train_df.dropna()
        regressor_impute_feature_cols = [
            col for col in feature_cols_list if col not in cols_to_impute_via_regression
        ]

        X = regressor_impute_train_df[regressor_impute_feature_cols]
        y = regressor_impute_train_df[col]

        regressor.fit(X, y)

        y_pred = regressor.predict(X)

        rmse = np.sqrt(mean_squared_error(y, y_pred))

        # In case need to cast to int, for example for number_of_dependents
        predicted_col = regressor.predict(imputed_df[regressor_impute_feature_cols])
        predicted_col = predicted_col.astype(cols_dtype[idx])

        imputed_df[col] = np.where(
            pd.isnull(imputed_df[col]), predicted_col, imputed_df[col]
        )

        imputer_dict[col] = {
            "regressor": regressor,
            "feature_cols": regressor_impute_feature_cols,
            "rmse": rmse,
        }

    return imputer_dict, imputed_df
