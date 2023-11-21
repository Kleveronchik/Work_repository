import requests as r
from bs4 import BeautifulSoup as bs
class WeatherParser:
    def __init__(self, url:str):
        self.Url:str = url
        self.Result:dict = {}
    def NbuParse(self, tag:str, attribute:str):
        response = r.get(self.Url)
        response_content = response.content
        html = bs(response_content, features="html.parser")
        tags = html.find(tag, attrs={'class': attribute})
        self.Result = tags.text