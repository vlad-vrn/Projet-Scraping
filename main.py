import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = "https://books.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('article', class_ = "product_pod")
aside = soup.find('aside')
for child in aside.children:
    print(child.text)