import string
import pandas as pd


def json_convertion(df, path):
    """
    Créer un json nested
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("first input is not a pandas Dataframe")
    if not isinstance(path, str):
        raise TypeError("second input is not a string")
    d = (
        df.groupby(["drug", "type"])["title", "date", "journal"]
        .apply(lambda x: x.to_dict("r"))
        .reset_index(name="data")
        .groupby("drug")["type", "data"]
        .apply(lambda x: x.set_index("type")["data"].to_dict())
    )
    d.to_json(path, indent=4)

    return True
