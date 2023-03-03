import streamlit as st
import requests as req

st.title('Taxi Fare Prediction')
'''Bonjour petit passager ! 🚕 '''

pickup_date = st.date_input('When is your ride ?')
pickup_time = st.time_input('At what time ?')
pickup_longitude = st.number_input('Pickup longitude ?')
pickup_latitude = st.number_input('Pickup latitude ?')
dropoff_longitude = st.number_input('Dropoff longitude ?')
dropoff_latitude = st.number_input('Dropoff latitude ?')
passenger_count = st.number_input('How many passengers ?',value=1)
pickup_datetime = f'{pickup_date.strftime("%Y-%m-%d")} {pickup_time.strftime("%H:%M:%S")}'


url = 'https://taxifare.lewagon.ai/predict'

params = {'pickup_datetime': pickup_datetime,
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': passenger_count}

request = req.get(url, params=params).json()
print(request)

''' Prepare the money 🤑 '''
st.write('Your fare is :')
st.write(request.get('fare'))