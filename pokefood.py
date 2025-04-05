import streamlit as st
import pandas as pd

# Load Pokémon data
@st.cache_data
def load_data():
    df = pd.read_csv("pokemon_edible.csv")
    return df

df = load_data()

# Constants
LEAN_FACTOR = 2.0   # grams of protein per attack point
FAT_FACTOR = 1.5    # grams of fat per HP point
PRICE_BASE = 10     # base price per kg for simplicity

st.title("🦴 Pokémon Meat Market 🥩")

pokemon_name = st.text_input("Enter a Pokémon name:")

if pokemon_name:
    # Case-insensitive search
    row = df[df["Name"].str.lower() == pokemon_name.lower()]
    
    if row.empty:
        st.error("Pokémon not found!")
    else:
        poke = row.iloc[0]
        
        if poke["Edible"] == 0:
            st.markdown(f"## ❌ {poke['Name']} is inedible!")
        else:
            attack = poke["Attack"]
            hp = poke["HP"]
            bmi = poke["BMI"]
            scarcity = poke["Scarcity"]
            
            protein_g = attack * LEAN_FACTOR
            fat_g = hp * FAT_FACTOR
            yield_factor = bmi / 100  # approximate meat yield
            scarcity_multiplier = 1 / scarcity if scarcity > 0 else 1  # prevent divide-by-zero
            
            # Price calculation
            price_per_kg = (protein_g + fat_g) * yield_factor * scarcity_multiplier
            price_per_kg = round(price_per_kg, 2)
            
            st.markdown(f"## 🍖 {poke['Name']} is edible!")
            st.markdown(f"**Meat Type:** {poke['Meat Type']}")
            st.markdown(f"**Protein:** {protein_g:.1f}g")
            st.markdown(f"**Fat:** {fat_g:.1f}g")
            st.markdown(f"**Yield Factor:** {yield_factor:.2f}")
            st.markdown(f"**Scarcity Multiplier:** {scarcity_multiplier:.2f}")
            st.markdown(f"### 💰 Estimated Market Price: ${price_per_kg}/kg")
