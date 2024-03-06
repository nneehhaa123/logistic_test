import pandas as pd
import pickle
import pytest 


def test_attribute():
    df = pd.read_csv("./data/insurance_data.csv")
    assert df.shape[1] == 2

@pytest.fixture()
def model():
    loaded_model = pickle.load(open("./Model/lr_model.pkl", "rb"))
    return loaded_model

def test_predict(model):

    # load the model from disk
    data = {"CLMAGE": 100}
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)
    print(prediction)
    assert prediction ==1