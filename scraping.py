from bs4 import BeautifulSoup
import requests
import string
import urllib
from json_parser import parser

class scraper:
    def __init__(self):
        super().__init__()

    def text_scraper(self):
        

        source = []
        final_text=""
        
        source.append(requests.get('https://g1.globo.com/sp/sao-paulo/noticia/2020/02/20/chuvas-colocam-zona-leste-de-sp-em-estado-de-atencao-para-alagamentos.ghtml').text)
        source.append(requests.get('https://noticias.uol.com.br/cotidiano/ultimas-noticias/2020/02/10/pontos-alagamentos-regioes-sao-paulo-chuva.htm').text)
        source.append(requests.get('https://g1.globo.com/sp/sao-paulo/noticia/2020/02/10/veja-pontos-de-alagamentos-em-manha-de-chuva-em-sp.ghtml').text)

        for link in source:
            soup = BeautifulSoup(link, 'lxml')

            final_text=final_text + soup.body.text.upper()

        return final_text

class matcher:
    def __init__(self):
        super().__init__()

    def retrieve(self):
        data_parser = parser()
        data = data_parser.parse()
        text_scraper = scraper()
        final_text = scraper.text_scraper()
        locations = []

        for info in data:
            if info["Value"].upper() in final_text:
                if info["Value"].upper not in locations:
                    locations.append(info)

        return locations
