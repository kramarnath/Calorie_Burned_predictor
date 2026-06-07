from flask import Flask, render_template, request
import joblib
from werkzeug import user_agent

app = Flask(__name__)
model = joblib.load('model.pkl')

# Both GET (initial view) and POST (form submissions) route to the same page
@app.route('/', methods=['GET', 'POST'])
def home():
    calories_prediction = None  # Default state when the page first loads
    user_inputs = None # Holds original inputs to send back to the user interface
    if request.method == 'POST':

        # 1. Capture inputs directly from HTML form fields
        gender = float(request.form.get('gender', 1)) 
        age = float(request.form.get('age', 25))
        height_cm = float(request.form.get('height', 170))
        weight_kg = float(request.form.get('weight', 70))
        duration = float(request.form.get('duration', 30))
        heart_rate = float(request.form.get('heart_rate', 80))
        body_temp = float(request.form.get('body_temp', 37))
        # initial inputs will get replaced by the user inputs
        
        # 2. Store them exactly as entered to preserve UI state
        user_inputs = {
            'gender': gender,
            'age': int(age),
            'height': int(height_cm),
            'weight': int(weight_kg),
            'duration': int(duration),
            'heart_rate': int(heart_rate),
            'body_temp': body_temp
        }

        # 3. Feature Engineering (BMI)
        height_m = height_cm / 100.0
        bmi = weight_kg / (height_m ** 2)

        # 4. Predict using the 8 features
        features = [gender, age, height_cm, weight_kg, duration, heart_rate, body_temp, bmi]
        prediction = model.predict([features])
        calories_prediction = round(float(prediction[0]), 2)

    # 5. Pass the calculated prediction variable directly into your HTML page template
    return render_template('index.html', calories=calories_prediction, inputs=user_inputs)

if __name__ == '__main__':
    app.run(debug=True)
