import requests
from bs4 import BeautifulSoup
from pprint import pprint

base_url = "https://books.toscrape.com/"

def goofy_get_stars_rating():
    with requests.Session() as session:
        response = session.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_= 'product_pod')
        ratings = [article.find('p')['class'] for article in articles]
        pprint(ratings)


def get_stars_rating_from_all():
    with requests.Session() as session:
        response = session.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.select('article.product_pod')
        for article in articles:
            #print(get_stars_raiting_from_article(article))
            get_id(article)

def get_stars_raiting_from_article(article):
    return article.select_one('p')['class']

def is_one_starred(article):
    if get_stars_raiting_from_article(article)[1] == 'One':
        return True
    return False

def get_id(article):
    link = article.select_one('h3').select_one('a')['href']
    link = link.split("_")
    link = link[1].split("/") #vraiment du grand brigandage
    return (link[0])

def main():
    with requests.Session() as session:
        response = session.get(base_url)
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.select('article.product_pod')
        for article in articles:
            if is_one_starred(article) == True:
                print(get_id(article))


main()