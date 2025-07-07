import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = "https://books.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

sidecat = soup.find('div', class_='side_categories')
categories_div = sidecat.find('ul').find('li').find('ul')
categories =[child.text.strip() for child in categories_div.children if child.name]

images = soup.find('section').find_all('img')
for image in images:
    print(image['src'])

#images1 = [child.text.strip() for child in images.children['src']]
#pprint(images1)