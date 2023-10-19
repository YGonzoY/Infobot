import telebot
from pyowm import OWM
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

#environment params
openWeatherToken = "b8e287577fea6f5c72132b3cceb1f581"   #do LESS than 1000 requests/day
bot = telebot.TeleBot("6311344470:AAFe2XZAJvPUQwHN7XcWgsdWvKqz7eNuB4o", parse_mode="html")



def getCnnNews():
    url = "https://edition.cnn.com/"
    client = ureq(url)
    pageHtml = client.read()
    client.close()

    pageSoup = soup(pageHtml, "html.parser")
    articles = pageSoup.find("div", {"class": "scope"})
    articles = articles.findAll("div", {"class": "container__headline container_lead-package__headline"})

    titles = list()
    i = 1
    for x in articles:
        title = x.find("span").text
        titles.append(title)
        #print(i, title, "\n")
        i = i + 1

    return titles

def getFoxNews():
    url = "https://www.foxnews.com/"
    client = ureq(url)
    pageHtml = client.read()
    client.close()

    pageSoup = soup(pageHtml, "html.parser")
    articles = pageSoup.find("div", {"class": "page"})
    articles = articles.find("div", {"class": "thumbs-2-7"})
    articles = articles.findAll("div", {"class": "info"})

    titles = list()
    i = 1
    for x in articles:
        title = x.find("a").text
        titles.append(title)
        #link = x.find("a")["href"]
        #titles[title] = link
        i = i + 1
    return titles

def getWeather(city):
    owm = OWM(openWeatherToken)
    weatherManager = owm.weather_manager()
    weather = weatherManager.weather_at_place(city).weather
    weatherInfo = f"""
{weather.detailed_status}
temperature - {weather.temperature('celsius')["temp"]}C
"""
    return weatherInfo


def printData():
    news = getCnnNews()
    for t in news:
        print(t, "\n")
    print(getWeather("Tula"))




@bot.message_handler(commands=["start"])
def startMessage(message):
    buttonList = {}
    bot.send_message(message.chat.id, """
to get weather type  /weather
to get news type    /news"""
                     )


@bot.message_handler(commands=["weather"])
def sendWeather(message):
    bot.send_message(message.chat.id, getWeather("Tula"))


@bot.message_handler(commands=["news"])
def sendNews(message):
    newsFox = getFoxNews()
    text = ""
    for new in newsFox:
        text += f"{new}\n"
    bot.send_message(message.chat.id, f"""
FOX:
    {text}
""", parse_mode = "html"

                     )

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
