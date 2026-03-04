import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

# =====================================================
# CREATE APP
# =====================================================
app = Flask(__name__)

# =====================================================
# LOAD MODEL & SCALER
# =====================================================
try:
    with open("min_max_scaler.sav", "rb") as f:
        scaler = pickle.load(f)

    with open("Bike_rental.sav", "rb") as f:
        rf = pickle.load(f)

    print("Scaler and model loaded successfully")

    # check scaler fitted
    if not hasattr(scaler, "scale_"):
        raise Exception("Scaler is not fitted.")

except Exception as e:
    print("MODEL LOAD ERROR:", e)
    scaler = None
    rf = None


# =====================================================
# HOME PAGE
# =====================================================
@app.route('/')
def home():
    return render_template('home.html')


# =====================================================
# PREDICTION ROUTE
# =====================================================
@app.route('/predict', methods=['POST'])
def predict():
    try:

        if scaler is None or rf is None:
            return render_template(
                "home.html",
                prediction_text="Model not loaded properly."
            )

        form = request.form.to_dict()

        # DATE FEATURE ENGINEERING
        date = pd.to_datetime(form["dteday"])
        year = date.year
        month = date.month
        day = date.day

        # FEATURE VECTOR (same order as training)
        data = [
            year,
            month,
            day,
            float(form["season"]),
            float(form["yr"]),
            float(form["mnth"]),
            float(form["holiday"]),
            float(form["weekday"]),
            float(form["workingday"]),
            float(form["weathersit"]),
            float(form["temp"]),
            float(form["atemp"]),
            float(form["hum"]),
            float(form["windspeed"]),
            float(form["casual"]),
            float(form["registered"]),
            float(form["cnt"]),
        ]

        final_input = scaler.transform(np.array(data).reshape(1, -1))
        prediction = rf.predict(final_input)[0]

        return render_template(
            "home.html",
            prediction_text=f"Predicted Bike Count: {prediction}"
        )

    except Exception as e:
        return render_template(
            "home.html",
            prediction_text=f"Error: {e}"
        )


# =====================================================
# RUN APP
# =====================================================
if __name__ == "__main__":
    app.run(debug=True)