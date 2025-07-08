import requests
from bs4 import BeautifulSoup
from pprint import pprint

initialUrl = "https://fondationdefrance.org/fr/tag-vulnerabilites"

soup = BeautifulSoup(requests.get(initialUrl).text, "html.parser")

columns = soup.find('div', id="template-amJs7jvN#2", class_="uk-margin")
text = columns.text.strip() if columns.name else ""

pprint(text)