from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

def getCnnNews():
    url = "https://edition.cnn.com/"
    client = ureq(url)
    page_html = client.read()
    client.close()

    page_soup = soup(page_html, "html.parser")
    articles = page_soup.find("div" , { "class" : "scope" })
    articles = articles.findAll("div" , {"class" : "container__headline container_lead-package__headline"})

    print(articles)
    i = 1
    for x in articles:
        title = x.find("span").text
        print(i, title, "\n")
        i=i+1

def getFoxNews():
    url = "https://www.foxnews.com/"
    client = ureq(url)
    page_html = client.read()
    client.close()

    page_soup = soup(page_html, "html.parser")
    articles = page_soup.find("div", {"class": "page"})
    articles = articles.findAll("div", {"class": "info"})

    print(articles)
    i = 1
    for x in articles:
        title = x.find("h3").text
        print(i, title, "\n")
        i = i + 1

getCnnNews()
