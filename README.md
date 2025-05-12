# ✈️ Flight Price Prediction System

A machine learning–based application that predicts airline ticket prices using real-world flight data. This project covers the complete ML workflow: data preprocessing, model training, performance evaluation, and deployment via a user-friendly Streamlit interface.


## 📌 Overview

Airfare pricing is influenced by a variety of factors including airline, travel dates, route, and number of stops. Accurate prediction of flight prices can benefit consumers and travel platforms alike. This project utilizes regression techniques to forecast flight ticket prices based on historical flight data.


## 🎯 Project Goals

- Extract and preprocess flight data for modeling.
- Engineer relevant features from raw data (e.g., duration, departure time).
- Train and evaluate robust machine learning models.
- Deploy the model through an interactive web application.


## 🧠 Model & Methodology

- **Model**: XGBoost Regressor (selected for its accuracy and efficiency)
- **Data Processing**:
  - Parsing date and time features
  - Duration conversion
  - Categorical encoding (Label/One-Hot)
- **Evaluation Metrics**:
  - R² Score
  - RMSE (Root Mean Squared Error)

> The final model is serialized as a `.pkl` file and integrated into the web app.



## 🗂️ Dataset

- **Source**: Public flight fare dataset (domestic routes)
- **Target Variable**: `Price`
- **Selected Features**:
  - Airline
  - Source and Destination
  - Total Stops
  - Date of Journey, Departure and Arrival Time
  - Duration



## 🛠️ Technologies Used

- **Programming Language**: Python 3.9+
- **Libraries**:  
  - pandas, numpy  
  - scikit-learn, xgboost  
  - seaborn, matplotlib (EDA)  
  - Streamlit (Deployment)


## 🚀 Application Deployment

### 🖥️ Local Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/flight-price-prediction.git
   cd flight-price-prediction
