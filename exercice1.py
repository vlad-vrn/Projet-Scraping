import requests
from bs4 import BeautifulSoup
from pprint import pprint

initialUrl = "https://books.toscrape.com/"
response = requests.get(initialUrl)

soup = BeautifulSoup(response.text, 'html.parser')

def find_number(url):
    responselink = requests.get(url)
    sub_soup = BeautifulSoup(responselink.text, 'html.parser')
    former = sub_soup.find('form', class_="form-horizontal")
    return former.find('strong').text.strip()

def main(n):
    aside_div = soup.find('div', class_="side_categories")
    categories = aside_div.find('ul').find('li').find('ul')
    for category in categories.children:
        #numb = find_number(category.get('href'))
        link = category.find('a')
        print(category.get('href'))
        #numb = find_number(link.get('href'))
        #if numb<n:
        #    print(category.text.strip())
main(5)
