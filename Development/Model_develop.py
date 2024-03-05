# import the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import pickle

# import the data
df = pd.read_csv("./data/insurance_data.csv")
X = df["age"].values.reshape(-1, 1)
Y = df["bought_insurance"].values.reshape(-1, 1)
train_x, test_x, train_y, test_y = train_test_split(
    X, Y, test_size=0.3, random_state=99
)
lr = LogisticRegression()
lr.fit(train_x, train_y)
y_pred = lr.predict(test_x)
print("Model Score: ", lr.score(test_y, y_pred))
print(confusion_matrix(test_y, y_pred))
with open("./Model/lr_model.pkl", "wb") as f:
    pickle.dump(lr, f)
