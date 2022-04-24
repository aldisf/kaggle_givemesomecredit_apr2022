import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import pointbiserialr

from src.constants import LABEL_COL, RANDOM_SEED, VAL_SIZE
from typing import List


def get_biserial_correlation_stats(
    train_df: pd.DataFrame,
    label_col: str,
    feature_col_list: List[str],
    should_plot: bool = True,
) -> pd.DataFrame:

    biserial_corr_dict = {
        "feature": [],
        "biserial_correlation": [],
    }

    corr_df = train_df.copy(deep=True).dropna()

    for feat in feature_col_list:
        corr = pointbiserialr(corr_df[label_col], corr_df[feat])
        biserial_corr_dict["feature"].append(feat)
        biserial_corr_dict["biserial_correlation"].append(corr.correlation)

    biserial_corr_df = pd.DataFrame(biserial_corr_dict)

    if should_plot:
        plt.figure()
        plt.title(f"Biserial Correlation of Features vs {LABEL_COL}", fontsize=14)
        sns.barplot(
            y="feature",
            x="biserial_correlation",
            data=biserial_corr_df.sort_values(by=["biserial_correlation"]),
            color="tab:red",
        )
        plt.show()

    return biserial_corr_df


def get_correlation_df(
    train_df,
    label_col: str,
    feature_col_list: List[str],
    should_plot: bool = True,
) -> pd.DataFrame:

    corr_df = train_df[[label_col] + feature_col_list].corr()

    if should_plot:
        plt.figure()
        plt.title("Correlation Heatmap", fontsize=14)
        sns.heatmap(corr_df)
        plt.show()

    return corr_df


def get_base_rf_auc_feature_importance(
    train_df: pd.DataFrame,
    label_col: str,
    feature_col_list: List[str],
    random_seed: int = RANDOM_SEED,
    val_size: float = VAL_SIZE,
):
    fit_df = train_df.copy(deep=True).dropna()

    X = fit_df[feature_col_list]
    y = fit_df[label_col]

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, random_state=random_seed, test_size=val_size
    )

    prelim_clf = RandomForestClassifier(max_depth=10)
    prelim_clf.fit(
        X=X_train,
        y=y_train,
    )

    prelim_train_pred = prelim_clf.predict_proba(X_train)
    prelim_val_pred = prelim_clf.predict_proba(X_val)
    prelim_train_roc_auc = roc_auc_score(
        y_true=y_train, y_score=prelim_train_pred[:, 1]
    )
    prelim_val_roc_auc = roc_auc_score(y_true=y_val, y_score=prelim_val_pred[:, 1])

    ft_importance_df = pd.DataFrame(
        {
            "feature": feature_col_list,
            "rf_feature_importance": prelim_clf.feature_importances_,
        }
    ).sort_values(by="rf_feature_importance", ascending=False)

    return prelim_clf, prelim_train_roc_auc, prelim_val_roc_auc, ft_importance_df
