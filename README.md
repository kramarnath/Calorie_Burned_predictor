# Calorie Burn Predictor

A machine learning web app that predicts calories burned during exercise based on personal attributes and workout duration. Built with **Scikit-learn** and **Streamlit**.

---

## Project Overview

This project compares two regression models — **Random Forest** and **Gradient Boosting** — to predict calorie expenditure. The best-performing model is deployed via a clean Streamlit web interface.

### Features used for prediction:
| Feature | Description |
|---|---|
| Gender | Male / Female |
| Age | Age in years |
| Height | Height in cm |
| Weight | Weight in kg |
| Duration | Exercise duration in minutes |

---

## Models Compared

| Model | MAE | MSE | R² Score |
|---|---|---|---|
| Random Forest | *(8.85331323015873)* | *(160.31123916878246)* | *(0.9602776208659054)* |
| Gradient Boosting | *(8.442765509451121)* | *(141.60539932412985)* | *(0.9649126075716636)* |

> Random Forest was selected for deployment based on lower MAE and higher R² score.

---

## Project Structure

```
calorie-burn-predictor/
│
├── app.py                          # Streamlit web app
├── calorie_burn_randomForest.py    # RF model training script
├── calorie_burn_gradientRegressor.py  # GB model training script
├── calorie_model.pkl               # Saved trained model
├── exercise.csv                    # Exercise dataset
├── calories.csv                    # Calories dataset
├── requirements.txt                # Python dependencies
└── README.md
```

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/calorie-burn-predictor.git
cd calorie-burn-predictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model (generates `calorie_model.pkl`)
```bash
python calorie_burn_randomForest.py
```

### 4. Launch the Streamlit app
```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

---

## Dataset

- **Source:** [Kaggle — Exercise and Calories Dataset](https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemo)
- `exercise.csv` — Gender, Age, Height, Weight, Duration, Heart Rate, Body Temp
- `calories.csv` — Calories burned per session

> Heart Rate and Body Temp were dropped since they are not available before a workout.

---

## Tech Stack

- **Python 3.10+**
- **Scikit-learn** — Model training & evaluation
- **Pandas / NumPy** — Data processing
- **Matplotlib / Seaborn** — Visualizations
- **Streamlit** — Web app deployment

---

## Sample Output

> For a 22-year-old Male, 172 cm, 68 kg, exercising for 30 minutes:
> **Predicted Calories Burned: ~245 kcal**

---

## Author

**Amarnath K R**  
[GitHub](https://github.com/your-username)
---

## License

This project is open source under the [MIT License](LICENSE).
