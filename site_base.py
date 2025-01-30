import requests
from bs4 import BeautifulSoup

class Site:
    def __init__(self, site):
        self.site = site
        self.news = []

    def update_news(self):
        if self.site.lower() == 'globo':
            url = 'https://www.globo.com/'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36'
            }
            page = requests.get(url, headers=headers)

            soup = BeautifulSoup(page.text, 'html.parser')
            noticias = soup.find_all('a')  # Removido [0] para pegar todos os links

            tg_class1 = 'post__title'
            tg_class2 = 'post-multicontent__link--title__text'
            
            news_dict_globo = {}

            for noticia in noticias:
                if noticia.h2 is not None:
                    h2_classes = noticia.h2.get('class', [])  # Evita erro se 'class' for None
                    if tg_class1 in h2_classes or tg_class2 in h2_classes:
                        news_dict_globo[noticia.h2.text.strip()] = noticia.get('href')


            # colocar outros sites

            return news_dict_globo  # Corrigido retorno

# Testando a classe
news_globo = Site('globo').update_news()
print(news_globo)
