from data import load_data
from model import build_model, train_model
from sklearn.metrics import mean_absolute_error
import joblib

X_train, y_train = load_data()
model = build_model()
model = train_model(model, X_train, y_train)

<<<<<<< HEAD
'''
=======
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

>>>>>>> 09505c31bfeb480946379b52894a831598e092ac
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: ${mae:.2f}")
'''