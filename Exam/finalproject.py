from repository import Repository
from parser import HtmlParser
from parser import WeatherParser
repo = Repository('exam.sl3', 5.0)

#1 CREATE TABLE
repo.Query('CREATE TABLE LINKS (id INTEGER PRIMARY KEY AUTOINCREMENT, link VARCHAR(50), name VARCHAR(20))')
repo.Query('CREATE TABLE RESULT (id INTEGER PRIMARY KEY AUTOINCREMENT, result VARCHAR(50))')

#2 INSERT INTO LINKS (name_of_fields) VALUES(set_of_values)
records = [
    ('https://bank.gov.ua/', 'nbu'),
    ('https://meteo.ua/34/kiev', 'weather')]
query = "INSERT INTO LINKS(link, name) VALUES(?, ?)"
repo.QueryMany(query, records)

#3.1 INSERT INTO RESULT (name_of_fields) VALUES(set_of_values)
res = repo.Execute('SELECT link FROM LINKS WHERE  id = 1')
parser = HtmlParser(res[0][0])
parser.NbuParse('div', 'index-page')
hrn = 1000
#hrn = int(input("Введіть суму (грн): "))
result = hrn/parser.Result['3']
kurs = parser.Result['3']
rDb = f'{result:.2f}'
resDB = f'Kurs $={kurs}, Hrn={hrn}, Result={rDb}'
query = f"INSERT INTO RESULT (result) VALUES('{resDB}')"
repo.Query(query)

#3.2 INSERT INTO RESULT (name_of_fields) VALUES(set_of_values)
res = repo.Execute('SELECT link FROM LINKS WHERE  id = 2')
parser = WeatherParser(res[0][0])
parser.NbuParse('div', 'weather-detail__main-temp js-weather-detail-value')
result = parser.Result
query = f"INSERT INTO RESULT (result) VALUES('{result}°C')"
repo.Query(query)