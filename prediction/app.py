# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:01:17 2020

"""


import pandas as pd
import streamlit as st

# from sklearn.linear_model import LogisticRegression
# from pickle import dump
from pickle import load

st.title("Model Deployment: Logistic Regression")

st.sidebar.header("User Input Parameters")


def user_input_features():
    # CLMSEX = st.sidebar.selectbox('Gender',('1','0'))
    # CLMINSUR = st.sidebar.selectbox('Insurance',('1','0'))
    # SEATBELT = st.sidebar.selectbox('SeatBelt',('1','0'))
    CLMAGE = st.sidebar.number_input("Insert the Age")
    # LOSS = st.sidebar.number_input("Insert Loss")
    data = {"CLMAGE": CLMAGE}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()
st.subheader("User Input parameters")
st.write(df)


# load the model from disk
loaded_model = load(open("./Model/lr_model.pkl", "rb"))

prediction = loaded_model.predict(df)
prediction_proba = loaded_model.predict_proba(df)

if st.button("Predict claim reimbursment"):
    st.subheader("Predicted Result")
    st.success("Yes" if prediction_proba[0][1] > 0.5 else "No")