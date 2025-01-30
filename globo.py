import requests
from bs4 import BeautifulSoup

globo_url = 'https://www.globo.com/'
page = requests.get(globo_url)

resposta = page.text

soup = BeautifulSoup(resposta, 'html.parser')

print(soup.title)

noticias = soup.find_all('h2', {'class': 'post__title'})

for noticia in noticias:
    print(noticia.text)