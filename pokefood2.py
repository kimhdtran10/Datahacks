import streamlit as st
import pandas as pd
from data import load_data
from model import build_model, train_model
from config import FEATURES

st.title("Pokémon Price Predictor")

X_train, y_train load_data()
model = build_model()
model = train_model(model, X_train, y_train)

inputs = []
for feature in x_train.columns.values.tolist():
    default = float(df[feature].mean())
    val = st.number_input(f"{feature}", value=default)
    inputs.append(val)

input_df = pd.DataFrame([inputs], columns=X_train.columns.values.tolist())
input_scaled = scaler.transform(input_df)
pred = model.predict(input_scaled)[0]

st.subheader(f"Predicted Price per lb: ${pred:.2f}")