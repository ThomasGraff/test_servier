import pandas as pd


def json_convertion(df, path):
    """
    Créer un json nested
    """
    assert isinstance(df, pd.DataFrame)
    d = (
        df.groupby(["drug", "type"])["title", "date", "journal"]
        .apply(lambda x: x.to_dict("r"))
        .reset_index(name="data")
        .groupby("drug")["type", "data"]
        .apply(lambda x: x.set_index("type")["data"].to_dict())
    )
    d.to_json(path)

    return True
