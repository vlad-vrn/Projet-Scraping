import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

def aside_ex():
    aside = soup.find('div', class_ = 'side_categories')
    categories = aside.find('ul').find('li').find('ul')
    for category in categories.children:
        if category.name:
            print(category.text.strip())

    print("MR LE FAIRE")

    category_list = [child.text.strip() for child in categories.children if child.name]
    pprint(category_list)

def get_src1():
    articles = soup.find('section').find('ol', class_='row')
    for article in articles.descendants:
        if article.name:
            print(article.get('src'))

def get_src_correc():
    images = soup.find('section').find_all('img')
    for image in images:
        print(image['src'])

def comp_list():
    category_img = soup.find('section').find_all('img')
    image_list = [child.get('src') for child in category_img]
    pprint(image_list)

def get_title():
    category_title = soup.find('section').find_all('a', title = True)
    title_list = [child.get('title') for child in category_title if child.get('title')]
    pprint(title_list)

def nul_0_nada_atroce():
    article_list = soup.find('section').find_all('article')
    for article in article_list:
        titlespace = article.find('h3').find('a')
        print(titlespace.get('title'))



