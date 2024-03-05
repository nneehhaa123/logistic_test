import pandas as pd




def test_attribute():
    df = pd.read_csv("./data/insurance_data.csv")
    assert df.shape[1] == 2
