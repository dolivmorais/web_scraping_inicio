import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scraping(uf:str):
    URL = f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html'
    browser = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36'}
    page = requests.get(URL, headers=browser)

    soup = BeautifulSoup(page.content, 'html.parser')

    indicadores = soup.select('.indicador')

    uf_dict = {
        dado.select('.ind-label')[0].text: dado.select('.ind-value')[0].text
        for dado in indicadores
    }

    return uf_dict


def limpar_texto_dict(dicionario):
    # Função para limpar o texto
    def limpar_texto(texto):
        # Remove os caracteres \xa0 (espaço não quebrável)
        texto_limpo = texto.replace('\xa0', ' ')
        
        # Remove o ano entre colchetes, como [2023]
        texto_limpo = re.sub(r'\s*\[\d{4}\]\s*', ' ', texto_limpo)
        
        # Remove espaços extras e trim (remove espaços no início e no final)
        texto_limpo = ' '.join(texto_limpo.split())
        
        return texto_limpo

    # Itera sobre o dicionário e aplica a limpeza nos valores
    for chave, valor in dicionario.items():
        if isinstance(valor, str):  # Verifica se o valor é uma string
            dicionario[chave] = limpar_texto(valor)
    
    return dicionario


cons = scraping('sp')

df = pd.DataFrame(cons.items(), columns=['Descricao', 'Valor'])

print(df)