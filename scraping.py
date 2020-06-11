from bs4 import BeautifulSoup
import requests
import string
import urllib

source = []
final_text=""
bairros=[]
ruas = []
source.append(requests.get('https://g1.globo.com/sp/sao-paulo/noticia/2020/02/20/chuvas-colocam-zona-leste-de-sp-em-estado-de-atencao-para-alagamentos.ghtml').text)
source.append(requests.get('https://noticias.uol.com.br/cotidiano/ultimas-noticias/2020/02/10/pontos-alagamentos-regioes-sao-paulo-chuva.htm').text)
source.append(requests.get('https://g1.globo.com/sp/sao-paulo/noticia/2020/02/10/veja-pontos-de-alagamentos-em-manha-de-chuva-em-sp.ghtml').text)

for link in source:
    soup = BeautifulSoup(link, 'lxml')

    final_text=final_text + soup.body.text.upper()

with open("bairrosSP.txt") as f:
    for line in f:
        if line.upper() in final_text:
            bairros.append(line)
            break        

with open("ruasSPsemPrefixo.txt") as f:
    for line in f:
        if line.upper() in final_text:
            ruas.append(line)
print(bairros)
print("---------")
print(ruas)
