
import pandas as pd
import pickle

def main():
    loaded_model = pickle.load(open("./Model/lr_model.pkl", "rb"))
    df = pd.read_csv("./data/insurance_data.csv")
    y1 = loaded_model.predict(df[['age']])
    model_score = loaded_model.score(df[['bought_insurance']], y1)
    print('Model score is :', model_score)
    return model_score
    
if __name__ =="__main__":
    main()