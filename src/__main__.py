import pandas as pd
import json
from cleaning import clean_data
from json_save import json_convertion
from transformation import mention_article, all_mentions


def main():
    # Load
    clinical_trials = pd.read_csv("./données/clinical_trials.csv")
    drugs = pd.read_csv("./données/drugs.csv")
    pubmed = pd.read_csv("./données/pubmed.csv")

    # Clean data
    drugs = clean_data(drugs)
    pubmed = clean_data(pubmed)
    clinical_trials = clean_data(clinical_trials)

    # Transform data
    df_pubmed = mention_article(drugs, pubmed)
    df_clinical_trials = mention_article(drugs, clinical_trials)
    df_final = all_mentions(df_pubmed, df_clinical_trials)

    # Convert data to json
    path = "data.json"
    json_convertion(df_final, path)

    # Journal qui mentionne le plus de médicaments différents
    with open("data.json", "r") as f:
        data = json.load(f)

    all_journal = []
    for drug in data:
        journal_drug = []
        # On parcourt les données de chaque journal
        for i in range(len(data[drug]["journal"])):
            journal_drug.append(data[drug]["journal"][i]["journal"])
        uniquejournal_drug = list(set(journal_drug))
        all_journal = all_journal + uniquejournal_drug
    print(
        "Journal qui mentionne le plus de médicaments différents: "
        + max(all_journal, key=all_journal.count)
    )


if __name__ == "__main__":
    main()
