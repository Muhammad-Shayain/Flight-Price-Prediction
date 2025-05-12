import streamlit as st
import pandas as pd
import pickle
import os

st.title("Flight Price Prediction")

# Load the trained model
model = None
try:
    model_file = 'Flight_Price_Prediction.pkl'
    if os.path.exists(model_file):
        with open(model_file, 'rb') as file:
            model = pickle.load(file)
        st.write("Model loaded successfully!")
    else:
        st.error("❌ Model file not found.")
except FileNotFoundError:
    st.error("❌ Could not find the model file.")
except Exception as e:
    st.error(f"❌ An error occurred while loading the model: {e}")

if model:
    st.write("Model loaded successfully. Now the interface should appear.")

    # Collecting user input
    Total_Stops = st.selectbox("Total Stops", [0, 1, 2, 3])
    Day_of_journey = st.date_input("Day of Journey").day
    Month_of_journey = st.selectbox("Month of Journey", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    Dept_hour = st.slider("Departure Hour", 0, 23)
    Dept_min = st.slider("Departure Minute", 0, 59)
    Arrv_hour = st.slider("Arrival Hour", 0, 23)
    Arrv_min = st.slider("Arrival Minute", 0, 59)
    Duration_hour = st.slider("Duration Hour", 0, 24)
    Duration_min = st.slider("Duration Minute", 0, 59)

    # Airline selection (one-hot encoding)
    airline_options = ['Air Asia', 'Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business', 
                       'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara', 'Vistara Premium economy']
    airline = st.selectbox("Select Airline", airline_options)
    airline_one_hot = [1 if airline == option else 0 for option in airline_options]

    # Source and Destination (one-hot encoding)
    source_options = ['Banglore', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai']
    source = st.selectbox("Select Source", source_options)
    source_one_hot = [1 if source == option else 0 for option in source_options]

    destination_options = ['Banglore', 'Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi']
    destination = st.selectbox("Select Destination", destination_options)
    destination_one_hot = [1 if destination == option else 0 for option in destination_options]

    # Show the inputs to make sure they are collected correctly
    st.write(f"Total Stops: {Total_Stops}, Day: {Day_of_journey}, Month: {Month_of_journey}, "
             f"Dept Hour: {Dept_hour}, Dept Min: {Dept_min}, Arrival Hour: {Arrv_hour}, "
             f"Arrival Min: {Arrv_min}, Duration Hour: {Duration_hour}, Duration Min: {Duration_min}")
    st.write(f"Airline: {airline}, Source: {source}, Destination: {destination}")

    # Layout: Create a button for prediction in a column layout
    col1, col2 = st.columns([1, 2])
    with col2:
        if st.button("Predict Price"):
            # Combine all the input values into a single DataFrame for prediction
            input_data = pd.DataFrame([[
                Total_Stops, Day_of_journey, Month_of_journey, Dept_hour, Dept_min, Arrv_hour, Arrv_min,
                Duration_hour, Duration_min, *airline_one_hot, *source_one_hot, *destination_one_hot
            ]], columns=[
                'Total_Stops', 'Day_of_journey', 'Month_of_journey', 'Dept_hour', 'Dept_min', 'Arrv_hour', 'Arrv_min',
                'Duration_hour', 'Duration_min', 'Airline_Air Asia', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
                'Airline_Jet Airways', 'Airline_Jet Airways Business', 'Airline_Multiple carriers', 
                'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet', 'Airline_Trujet', 'Airline_Vistara', 
                'Airline_Vistara Premium economy', 'Source_Banglore', 'Source_Chennai', 'Source_Delhi', 'Source_Kolkata',
                'Source_Mumbai', 'Destination_Banglore', 'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad', 
                'Destination_Kolkata', 'Destination_New Delhi'
            ])
            st.write("Input data for prediction:")
            st.write(input_data)

            # Make prediction
            try:
                prediction = model.predict(input_data)
                st.write(f"Predicted Flight Price: ₹{prediction[0]:,.2f}")
            except Exception as e:
                st.error(f"❌ Error during prediction: {e}")
