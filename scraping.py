from bs4 import BeautifulSoup
import requests

source = requests.get('https://facens.br/home').text

soup = BeautifulSoup(source, 'lxml')

body_text = soup.body.text

print(body_text)