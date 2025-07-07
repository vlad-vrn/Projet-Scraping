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
    return int(former.find('strong').text.strip())

def main(n):
    aside_div = soup.find('div', class_="side_categories")
    categories = aside_div.find('ul').find('li').find('ul')
    links = categories.find_all('a')
    for link in links:
        numb = find_number(initialUrl + link['href'])
        if numb<n:
            print(link.text.strip())
main(2)
