from flask import Flask, render_template, request
import requests 
import joblib
import numpy as np  
import sklearn
from sklearn.preprocessing import StandardScaler
import pandas as pd
import os
from twilio.rest import Client

app = Flask(__name__)

model = joblib.load(filename='random_forest_model.joblib')

@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
	if request.method == 'POST':
		longitude = float(request.form['longitude'])
		latitude = float(request.form['latitude'])
		day_of_week = int(request.form['day_of_week'])
		speed_limit = int(request.form['speed_limit'])
		light_conditions = int(request.form['light_conditions'])
		weather_conditions = int(request.form['weather_conditions'])
		road_surface_conditions = int(request.form['road_surface_conditions'])
		vehicle_type = int(request.form['vehicle_type'])
		age_of_driver = np.log(int(request.form['age_of_driver']))
		age_of_vehicle = np.log(int(request.form['age_of_vehicle']))
		prediction = model.predict(pd.DataFrame(np.array([longitude, latitude, day_of_week,
                                                     speed_limit, light_conditions, weather_conditions
                                                     , road_surface_conditions, vehicle_type,
                                                      age_of_driver, age_of_vehicle]).reshape(1,10), 
                                           columns=['Longitude',
                                                    'Latitude',
                                                    'Day_of_week',
                                                    'Speed_limit',
                                                    'Light_Conditions',
                                                    'Weather_Conditions',
                                                    'Road_Surface_Conditions',
                                                    'Vehicle_Type',
                                                    'Age_of_Driver',
                                                    'Age_of_Vehicle']))
		result = prediction[0]
		if result not in [0,1,2,3]:
			return render_template('index.html',prediction_texts="There was some error!")
		else:
			account_sid = 'ACa8f4c6fa152d4936c5d03ae753618c0'
			auth_token = 'cd5a1dd38aa523c890e7699574c56ff'
			client = Client(account_sid, auth_token)

			message = client.messages \
                .create(
                     body=f"severity of accident is {result}, at longitude: {longitude} and latitude: {latitude}",
                     from_='+14704358193',
                     to='+917897732600'
                 )

			print(message.sid)
			return render_template('index.html',prediction_text="severity of accident is {}".format(result))
	else:
		return render_template('index.html')
