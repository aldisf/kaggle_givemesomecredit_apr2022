import time
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score


def train_and_val_clf(
    clf_class,
    X_train,
    y_train,
    X_val,
    y_val,
    clf_kwargs=dict(),
):
    clf = clf_class(**clf_kwargs)
    train_start_time = time.time()
    clf.fit(X_train, y_train)
    training_time = np.round(time.time() - train_start_time, 2)

    train_query_start_time = time.time()
    y_train_pred = clf.predict_proba(X_train)[:, 1]
    train_query_time = np.round(time.time() - train_query_start_time, 2)

    y_val_pred = clf.predict_proba(X_val)[:, 1]

    train_roc_auc = roc_auc_score(y_train, y_train_pred)
    val_roc_auc = roc_auc_score(y_val, y_val_pred)

    return clf, training_time, train_query_time, train_roc_auc, val_roc_auc


def ensemble_predict_proba(
    model_clf_dict: dict,
    X: pd.DataFrame,
):
    pred = pd.DataFrame(index=X.index)
    pred["Probability"] = np.zeros(len(X))

    denominator = 0

    for modelname, model_dict in model_clf_dict.items():

        model_weight = model_dict.get("ValROC-AUC")
        model_clf = model_dict.get("clf")

        pred["Probability"] += model_clf.predict_proba(X)[:, 1] * model_weight

        denominator += model_weight

    pred["Probability"] /= denominator

    return pred
