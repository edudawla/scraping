###...Metodo 1
###...Separei uma classe dentro da Div.
###...Separei a tag <a> e transformei em String
###...Quebrei a lista por ',' usando a biblioteca RE
###...Falta terminar e fazer o CRUD
import requests
from bs4 import BeautifulSoup
import re
url = 'https://www.sjc.sp.gov.br/servicos/mobilidade-urbana/novos-horarios-do-transporte-publico/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
#dentro da div, encontrar a classe
conteudo = soup.find_all('div', class_='sec_serv_conteudo_box')

for lista in conteudo:
    resultado = str(lista.find_all('a'))    #lista com dados separados por virgula

novalista = re.split(',',resultado)     #quebra da lista por virgula

"""
###...Metodo 2
###...Separei uma classe dentro da Div.
###...Separei a tag <a> e depois iterei o next_element até encontrar o titulo
###...Falta terminar e fazer o CRUD

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.sjc.sp.gov.br/servicos/mobilidade-urbana/novos-horarios-do-transporte-publico/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#dentro da div, encontrar a classe
conteudo = soup.find_all('div', class_='sec_serv_conteudo_box')

for lista in conteudo:
    resultado = lista.find_all('a')   
        for lista2 in resultado:
        print(final.next_element)

"""
