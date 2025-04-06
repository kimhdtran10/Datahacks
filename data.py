import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from config import FEATURES, TARGET, DATA_PATH

def load_data():
    df = pd.read_csv('train_data.csv')
    df = df[(df['Edible'] == 1) & (df[TARGET] > 0)]
    X_train = df.drop('Price per lb', axis=1)
    y_train = df['Price per lb']
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    return X_train, y_train