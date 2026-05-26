import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

exercise = pd.read_csv('../exercise.csv')
calories = pd.read_csv('../calories.csv')

df = pd.concat([exercise, calories['Calories']], axis=1)
df.drop(columns=['User_ID'], inplace=True)

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender']) # Encoded the Gender into 1 and 0
df['BMI'] = df['Weight'] / ((df['Height']/100)**2) # Added BMI as a Feature

X = df.drop(columns=['Calories'])
y = df['Calories'] # y = calories
# Train, Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42)
# Fradient Boosting regressor
gb = GradientBoostingRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=5,
    random_state=42
)
gb.fit(X_train, y_train)
gb_pred = gb.predict(X_test) # test Prediction

print("GRADIENT BOOSTING")

print("MAE:",
      mean_absolute_error(y_test, gb_pred))

print("RMSE : ", np.sqrt(mean_squared_error(y_test, gb_pred)))

print("R2:",
      r2_score(y_test, gb_pred))

# Feature Importance
print("GRADIENT BOOSTING")

importance = gb.feature_importances_

features = X.columns

imp_df = pd.DataFrame({
    'Feature': features,
    'Importance': importance
})

imp_df = imp_df.sort_values(
    by='Importance',
    ascending=False
)

print(imp_df)

plt.figure(figsize=(8,6))

plt.barh(
    imp_df['Feature'],
    imp_df['Importance']
)

plt.title("Gradient Boosting Feature Importance")

plt.show()