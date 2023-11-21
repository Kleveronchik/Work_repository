from repository import Repository
import time
from parser import WeatherParser
repo = Repository('weather.sl3', 5.0)

#1 CREATE TABLE
repo.Query('CREATE TABLE WEATHER (id INTEGER PRIMARY KEY AUTOINCREMENT, date_time VARCHAR(50), temperature VARCHAR(20))')
#3.2 INSERT INTO WEATHER (name_of_fields) VALUES(set_of_values)
while True:
    date_time = time.ctime()
    parser = WeatherParser("https://meteo.ua/34/kiev")
    parser.NbuParse('div', 'weather-detail__main-temp js-weather-detail-value')
    temp_result = parser.Result
    query = f"INSERT INTO WEATHER (date_time, temperature) VALUES('{date_time}', '{temp_result}°C')"
    repo.Query(query)
    print(f"{date_time} Table updated!")
    time.sleep(1799) #Update every 30 minutes