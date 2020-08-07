import requests
from bs4 import BeautifulSoup

url = 'https://www.sjc.sp.gov.br/servicos/mobilidade-urbana/novos-horarios-do-transporte-publico/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
#dentro da div, encontrar a classe
lista = soup.find_all('div', class_='sec_serv_conteudo_box')

for novalista in lista:
    print(novalista.find_all('a')




"""
novalista = re.split('<a',lista)
print(novalista)

for i in novalista:
    print(i)


#armazenar arquivo em uma variavel
resultado = []
for titulos in lista:
    resultado = titulos.find_all('a')
    #print(resultado)




#print(lista)




#novo= re.split(',',lista)

for i in novo:
    print(i)

for titulos in lista:
    resultado = titulos.find_all('a')


endereco = 'https://www.sjc.sp.gov.br'

#imprim
for link in resultado:
    print(link.get('href'))


#print(lista)

#print(r.text)
"""
