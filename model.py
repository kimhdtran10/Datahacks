from sklearn.neural_network import MLPRegressor

def build_model():
    return MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model