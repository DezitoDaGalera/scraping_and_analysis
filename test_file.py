from bs4 import BeautifulSoup
import requests
import string
import scraping

matcher_instance = scraping.matcher()
data = matcher_instance.retrieve()
print(data)