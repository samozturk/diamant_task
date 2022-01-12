from pickle import load

from pandas import read_csv


MODEL_PATH = "model.pickle"
DATA_PATH = "data.csv"


if __name__ == "__main__":
    # load model and data
    with open(MODEL_PATH, "rb") as file_handle:
        model = load(file_handle)
    data = read_csv(DATA_PATH, sep=";")

    # predict binary labels
    features = data.drop(["Customer", "bankauszug_Nummer", "op_DVBuchungsnummer", "Target"], axis=1)
    data["Prediction"] = model.predict(features)

    # evaluate on bsi level
    hits = []
    for _, single_bsi_data in data.groupby(["Customer", "bankauszug_Nummer"]):
        hits.append(all(single_bsi_data["Prediction"] == single_bsi_data["Target"]))
    print(f"BSI Accuracy: {sum(hits) / len(hits)}")
