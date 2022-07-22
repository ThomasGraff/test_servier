from typing import Type
import pandas as pd


def clean_data(df):
    """
    Supprimer les colonnes inutiles
    Supprimer les lignes ayant des données nécessaires manquantes
    Modifier les noms de colonnes pour uniformiser
    Modifier les string avec des erreurs si nécessaire
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input is not a pandas Dataframe")

    df = df.drop(["id", "atccode"], axis=1, errors="ignore")

    if "drug" in df.columns:
        df = df[df["drug"].notna()]
        df["drug"] = df.drug.str.lower()
    if "title" in df.columns:
        df = df[df["title"].notna()]
        df["title"] = df.title.str.lower()
    if "scientific_title" in df.columns:
        df.rename({"scientific_title": "title"}, axis=1, inplace=True)
        df = df[df["title"].notna()]
        df["title"] = df.title.str.lower()
        value = "Journal of emergency nursing"
        df["journal"][df["journal"] == value + "\\xc3\\x28"] = value

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
        df = df[df["date"].notna()]
        df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    assert isinstance(df, pd.DataFrame)
    return df
