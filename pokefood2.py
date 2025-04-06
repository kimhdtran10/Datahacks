import streamlit as st
import pandas as pd
import joblib
import os
from config import FEATURES

st.title("Pokémon Price Predictor")

if not os.path.exists("model.pkl") or not os.path.exists("scaler.pkl"):
    st.error("Model not found. Please run pokefood.py first to train and save the model.")
    st.stop()

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
df = pd.read_csv("pokemon_edible.csv")
df = df[(df['Edible'] == 1) & (df['Price per lb'] > 0)]

st.header("🔍 Look up a Pokémon")
name_query = st.text_input("Enter Pokémon name (e.g. Bulbasaur)")

if name_query:
    match = df[df['Name'].str.lower() == name_query.lower()]
    if not match.empty:
        row = match.iloc[0]
        input_features = row[FEATURES].values.reshape(1, -1)
        input_scaled = scaler.transform(input_features)
        pred = model.predict(input_scaled)[0]
        pred = max(0, pred)

        st.subheader(f"Price per lb: ${pred:.2f}")

        # Macros: use stats to infer macronutrients
        protein = row['Attack'] * 0.6
        fat = row['HP'] * 0.2
        carbs = row['Scarcity'] * 2 

        st.markdown("### 🥩 Nutritional Estimate (per 100g)")
        st.write(f"- Protein: {protein:.1f}g")
        st.write(f"- Fat: {fat:.1f}g")
        st.write(f"- Carbs: {carbs:.1f}g")
    else:
        st.warning("No matching Pokémon found or not edible.")