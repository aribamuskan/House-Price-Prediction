import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# 1. Load Dataset
# ==========================================

data = pd.read_csv("dataset/house_data.csv")

print("Full Dataset:")
print(data)

print("\nFirst 5 Rows:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nDataset Information:")
print(data.info())

print("\nDataset Statistics:")
print(data.describe())


# ==========================================
# 2. Separate Features and Target
# ==========================================

X = data[["area_sqft", "bedrooms", "bathrooms", "age"]]

y = data["price"]

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())


# ==========================================
# 3. Split Data into Training and Testing
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# ==========================================
# 4. Create Linear Regression Model
# ==========================================

model = LinearRegression()


# ==========================================
# 5. Train Model
# ==========================================

model.fit(X_train, y_train)

print("\nModel Training Completed!")


# ==========================================
# 6. Make Predictions
# ==========================================

y_pred = model.predict(X_test)

print("\nPredicted Prices:")
print(y_pred)


# ==========================================
# 7. Evaluate Model
# ==========================================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)


# ==========================================
# 8. Model Coefficients
# ==========================================

print("\nCoefficients:")
print(model.coef_)

print("\nIntercept:")
print(model.intercept_)


# ==========================================
# 9. Actual vs Predicted Prices
# ==========================================

results = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})

print("\nActual vs Predicted:")
print(results)


# ==========================================
# 10. Test Houses
# ==========================================

print("\nTest Houses:")
print(X_test)


# ==========================================
# 11. Predict Price for a New House
# ==========================================

new_house = pd.DataFrame({
    "area_sqft": [2000],
    "bedrooms": [4],
    "bathrooms": [3],
    "age": [10]
})

predicted_price = model.predict(new_house)

print("\nNew House:")
print(new_house)

print("\nPredicted Price:", predicted_price[0])
# ==========================================
# 13. Save Trained Model
# ==========================================

import joblib

joblib.dump(model, "house_price_model.pkl")

print("\nModel saved successfully!")