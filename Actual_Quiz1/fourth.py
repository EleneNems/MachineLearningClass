import numpy as np
import pandas as pd
import mysql.connector

city = ['Tbilisi', 'Gori', 'Batumi', 'Kutaisi', 'Khashuri']
cityCol = [np.random.choice(city) for _ in range(10)]
temp = np.random.randint(0, 41, 10)
hum = np.random.randint(20, 101, 10)
Aqi = np.random.randint(0, 501, 10)

weather = pd.DataFrame(
    {
        'City': cityCol,
        'Temp': temp,
        'Humidity': hum,
        'AQI': Aqi
    }
)

for i, row in weather.iterrows():
    if row['AQI'] <= 50:
        weather.loc[i, 'AQI_Cat'] = 'Good'
    elif row['AQI'] <= 100:
        weather.loc[i, 'AQI_Cat'] = 'Moderate'
    elif row['AQI'] <= 150:
        weather.loc[i, 'AQI_Cat'] = 'Unhealthy for Sensitive'
    elif row['AQI'] <= 200:
        weather.loc[i, 'AQI_Cat'] = 'Unhealthy'
    elif row['AQI'] <= 300:
        weather.loc[i, 'AQI_Cat'] = 'Very Unhealthy'
    else:
        weather.loc[i, 'AQI_Cat'] = 'Hazardous'

weather.to_excel('weather.xlsx', index=False)
print(weather.groupby(by='City')['Temp'].max())
print(weather.groupby(by='City')['AQI'].mean())
print(weather[weather['AQI'] > 150])
sortedData = weather.sort_values(by='Temp', ascending=False)
print(sortedData.head(5))

mydb = mysql.connector.connect(
    user='root',
    host='localhost',
    password='',
    database='ml_db'
)

InsertCommand = 'insert into city_weather(city, temperature, humidity, AQI, AQI_Category) values(%s, %s, %s, %s, %s)'
