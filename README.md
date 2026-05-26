# Calories Burn Prediction Using Machine Learning

## Project Overview

This project predicts calories burned during exercise using Machine Learning models.

The project compares multiple regression algorithms:
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

The final deployed model uses XGBoost because it achieved the best performance.

---

## Dataset

Dataset used:
- exercise.csv
- calories.csv

Source:
Kaggle Calories Burn Prediction Dataset

---

## Features Used

- Gender
- Age
- Height
- Weight
- Duration
- Heart Rate
- Body Temperature
- BMI (Engineered Feature)

---

## Feature Engineering

BMI was added using:

BMI = Weight / Height²

This improved prediction performance.

---

## Machine Learning Models

### 1. Random Forest Regressor
Ensemble learning using multiple decision trees.

### 2. Gradient Boosting Regressor
Sequential boosting model improving previous errors.

### 3. XGBoost Regressor
Advanced boosting algorithm with regularization and optimized tree learning.

---

## Model Evaluation Metrics

The following metrics were used:

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## Final Results

| Model | MAE | RMSE | R² |
|------|------|------|------|
| Random Forest | 1.7524 | 2.7448 | 0.9981 |
| Gradient Boosting | 1.0489 | 1.4854 | 0.9994 |
| XGBoost | 0.9286 | 1.3212 | 0.9995 |

XGBoost achieved the best performance.

---

## Visualizations

The project includes:
- Correlation Heatmap
- Feature Importance Graph
- Actual vs Predicted Plot
- Model Comparison Graph

---

## Deployment

The final model was deployed using:
- Streamlit
- Streamlit Community Cloud

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Streamlit

---

## How to Run

Install requirements:

pip install -r requirements.txt

Run Streamlit app:

streamlit run app.py
