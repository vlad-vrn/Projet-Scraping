import requests
from bs4 import BeautifulSoup
from pprint import pprint

initialUrl = "https://fondationdefrance.org/fr/tag-vulnerabilites"

soup = BeautifulSoup(requests.get(initialUrl).text, "html.parser")
columns = soup.find('div', id="template-amJs7jvN#2", class_="uk-margin")


def func1():
    text = columns.text.strip() if columns.name else ""
    pprint(text)



#for column in columns.children:
#    title = column.find('h3').find('a')
#    if title.name:
#        pprint(title.text.strip())

#title = columns.find('h3').find('a')
#pprint(title.text.strip())

def title_extraction():
    for a in columns.find_all('h3'):
        title = a.find('a')
        if title.name:
            pprint(title.text.strip())


def mr_le_faire():
    articles_h3 = columns.find_all('h3')
    titles_list = [title.text.strip() for title in articles_h3 if title.name]
    return titles_list

#def get_next_url():




mr_le_faire()