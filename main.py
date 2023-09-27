from pyowm import OWM
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

#environment params
openWeatherToken = "b8e287577fea6f5c72132b3cceb1f581"   #do LESS than 1000 requests/day


def getCnnNews():
    url = "https://edition.cnn.com/"
    client = ureq(url)
    pageHtml = client.read()
    client.close()

    pageSoup = soup(pageHtml, "html.parser")
    articles = pageSoup.find("div", {"class": "scope"})
    articles = articles.findAll("div", {"class": "container__headline container_lead-package__headline"})

    print(articles)
    i = 1
    for x in articles:
        title = x.find("span").text
        print(i, title, "\n")
        i=i+1

def getFoxNews():
    url = "https://www.foxnews.com/"
    client = ureq(url)
    pageHtml = client.read()
    client.close()

    pageSoup = soup(pageHtml, "html.parser")
    articles = pageSoup.find("div", {"class": "page"})
    articles = articles.findAll("div", {"class": "info"})

    print(articles)
    i = 1
    for x in articles:
        title = x.find("h3").text
        print(i, title, "\n")
        i = i + 1

def getWeather(city):
    owm = OWM(openWeatherToken)
    weatherManager = owm.weather_manager()
    weather = weatherManager.weather_at_place(city).weather

    weatherInfo = f"""
                {weather.detailed_status}
                temperature - {weather.temperature('celsius')["temp"]}C
                """


    print(weatherInfo)



getWeather("Tula, RU")
