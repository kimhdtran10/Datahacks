from data import load_data
from model import build_model, train_model

X_train, X_test, y_train, y_test, scaler, df = load_data()
model = build_model(X_train.shape[1])
model = train_model(model, X_train, y_train)

loss, mae = model.evaluate(X_test, y_test)
print(f"Mean Absolute Error: ${mae:.2f}")