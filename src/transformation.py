import pandas as pd


def mention_article(drugs, df):
    """
    Sélectionner les articles où sont mentionnées les drogues
    """
    if not isinstance(drugs, pd.DataFrame):
        raise TypeError("first input is not a pandas Dataframe")
    if not isinstance(df, pd.DataFrame):
        raise TypeError("second input is not a pandas Dataframe")
    df = drugs.merge(df, how="cross")
    df["drug_title"] = df.apply(lambda x: x.drug in x.title, axis=1)
    df = df[df["drug_title"] == True]
    df.pop("drug_title")

    return df


def all_mentions(df_pubmed, df_clinical_trial):
    """
    Sélectionner les journaux où sont mentionnées les drogues
    Concaténer tous les dataframes
    """
    if not isinstance(df_pubmed, pd.DataFrame):
        raise TypeError("first input is not a pandas Dataframe")
    if not isinstance(df_clinical_trial, pd.DataFrame):
        raise TypeError("second input is not a pandas Dataframe")
    df_journal = pd.concat([df_pubmed, df_clinical_trial])[["drug", "date", "journal"]]
    df = pd.concat(
        [df_pubmed, df_clinical_trial, df_journal],
        keys=("pubmed", "clinical_trial", "journal"),
        axis=0,
    ).reset_index(0)
    df.columns = ["type", "drug", "title", "date", "journal"]

    return df
