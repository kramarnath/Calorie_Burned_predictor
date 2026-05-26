import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from xgboost import XGBRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import (mean_absolute_error,
    mean_squared_error,
    r2_score)

exercise = pd.read_csv('../exercise.csv') # Imported DataSet
calories = pd.read_csv('../calories.csv') # Imported DataSet

df = pd.concat([exercise, calories['Calories']], axis=1) # Merge the Calorie Data Column to the Exercise Dataset
df.drop(columns=['User_ID'], inplace=True) # Dropped User ID

# Encoding
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender']) # Encoded the Gender into 1 and 0
df['BMI'] = df['Weight'] / ((df['Height']/100)**2) # Added BMI as a Feature

X = df.drop(columns=['Calories']) # Dropped Calories Column
y = df['Calories'] # y = calories

# Train, Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42)

xgb = XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42)
xgb.fit(X_train, y_train)
xgb_pred = xgb.predict(X_test)

# MAE, RMSE and R2 Values
print("XGBOOST")
print("MAE:",mean_absolute_error(y_test, xgb_pred))
print("RMSE : ", np.sqrt(mean_squared_error(y_test, xgb_pred)))
print("R2:",r2_score(y_test, xgb_pred))

# Feature Importance
importance = xgb.feature_importances_
features = X.columns
imp_df = pd.DataFrame({
    'Feature': features,
    'Importance': importance})
imp_df = imp_df.sort_values(
    by='Importance',
    ascending=False)
print(imp_df)
plt.figure(figsize=(8,6))
plt.barh(
    imp_df['Feature'],
    imp_df['Importance'])
plt.title("XGBoost Feature Importance")
plt.show()

# Actual vs Prediction plot
plt.figure(figsize=(8,6))
plt.scatter(y_test, xgb_pred)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r')
plt.xlabel("Actual Calories")
plt.ylabel("Predicted Calories")
plt.title("XGBoost: Actual vs Predicted")
# save plot automatically to project folder
plt.savefig('xgb_Actual_vs_Predicted_Plot.png', dpi=300, bbox_inches='tight')
plt.show()

# Residual plot
residuals = y_test - xgb_pred
plt.figure(figsize=(8,6))
plt.scatter(xgb_pred, residuals)
plt.axhline(y=0, color='r')
plt.xlabel("Predicted Calories")
plt.ylabel("Residuals")
plt.title("XGBoost Residual Plot") # Residual = Actual − Predicted
# save plot automatically to project folder
plt.savefig('xgb_residual_plot.png', dpi=300, bbox_inches='tight')
plt.show()