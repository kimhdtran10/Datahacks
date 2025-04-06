import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from config import FEATURES, TARGET, DATA_PATH

def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df[(df['Edible'] == 1) & (df[TARGET] > 0)]
    X = df[FEATURES]
    y = df[TARGET]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.15, random_state=42)
    return X_train, X_test, y_train, y_test, scaler, df