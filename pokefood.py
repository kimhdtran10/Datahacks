from data import load_data
from model import build_model, train_model
from sklearn.metrics import mean_absolute_error

X_train, X_test, y_train, y_test, scaler, df = load_data()
model = build_model()
model = train_model(model, X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: ${mae:.2f}")