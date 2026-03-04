# Bike_rental

#  Bike Rental Demand Prediction

##  Project Overview

This project predicts **bike rental demand** based on environmental and seasonal factors using a Machine Learning model.
A **Flask web application** allows users to input weather and date information and receive a predicted bike rental count.

The model analyzes features such as temperature, humidity, windspeed, season, and date to estimate how many bikes will be rented.

---

##  Machine Learning Model

The model was trained using the **Bike Sharing Dataset** and predicts the number of bike rentals for a given day.

**Algorithm Used**

* Random Forest Regressor
* GradientBoostingRegressor
* DecisionTreeRegressor
* LinearRegression

**Preprocessing**

* Feature engineering from date (`year`, `month`, `day`)
* MinMax Scaling
* Data cleaning and transformation
---

##  Features Used

* season
* year
* month
* holiday
* weekday
* workingday
* weather situation
* temperature
* feels-like temperature
* humidity
* windspeed
* extracted date features (year, month, day)

---

## 🖥️ Web Application

The Flask web app allows users to input:

* Date
* Season
* Year
* Month
* Holiday
* Weekday
* Working day
* Weather condition
* Temperature
* Feels-like temperature
* Humidity
* Windspeed

The application then predicts the **expected bike rental count**.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/Bike_rental.git
cd Bike_rental
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Flask application

```
python app.py
```
---

## 📊 Dataset

Dataset used: **Bike Sharing Dataset**

It contains daily and hourly records of bike rentals along with weather and seasonal information.

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML/CSS
* Jupyter Notebook

---

## 📈 Future Improvements

* Add model evaluation metrics in the UI
* Deploy the application on cloud (Render / AWS / Heroku)
* Improve UI with better styling
* Add hourly prediction capability

---



