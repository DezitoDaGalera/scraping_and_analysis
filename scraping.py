from bs4 import BeautifulSoup
import requests

source = requests.get('https://facens.br/home').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())