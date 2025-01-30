from site_base import *
import os
from threading import Thread
import time
from datetime import datetime
import sys
import pickle
import webbrowser
from math import ceil

from pytimedinput import timedInput

class News:
    def __init__(self):
        self.dict_site = {}
        self.all_sites = ['globo']

        self.screen = 0
        self.kill = False

        self.news = self._read_file('news') if 'news' in os.listdir() else []
        self._update_file(self.news, mode='news')
        self.sites = self._read_file('sites') if 'sites' in os.listdir() else []
        self._update_file(self.sites, mode='sites')

        for site in self.sites:
            self.dict_site[site] = Site(site)

        self.news_thread = Thread(target=self.update_news)
        self.news_thread.setDaemon(True)
        self.news_thread.start()

    def _update_file(self,lista, mode='news'):
        with open(mode, 'wb') as fp:
            pickle.dump(lista, fp)

    def _read_file(self, mode='news'):
        with open(mode, 'rb') as fp:
            n_lista = pickle.load(fp)   
            return n_lista
        
    def _receive_command(self, valid_commands, timeout=30):
        command, timed = timedInput('>>', timeout)
        while command.lower() not in valid_commands and not timed:
            print('Comando inválido tente novamente')
            command, timed = timedInput('>>', timeout)
        command = 0 if command == '' else command
        return command
    
    def main_loop(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            match self.screen:
                case 0:
                    print('Bem vindo ao News')
                    print('Selecione uma opção:')
                    print('')
                    print("1 - Ultimas noticias'\n2. Adicoionar site\n3. Remover site\n4. Fechar o news")
                    self.screen = int(self._receive_command(['1', '2', '3', '4'], 5))
                    print(self.screen,type(self.screen))

                case 1:
                    pass

                case 2:
                    pass

                case 3:
                    pass

                case 4:
                    self.kill = True
                    sys.exit()
                    

    def update_news(self):
        while not self.kill:
            #print('update news')
            for site in self.sites:
                self.dict_site[site].update_news()

                for key, value in self.dict_site[site].news.items():
                    dict_aux = {}
                    dict_aux['data'] = datetime.now()
                    dict_aux['fonte'] = site
                    dict_aux['materia'] = key
                    dict_aux['link'] = value

                    if len(self.news) == 0:
                        self.news.insert(0, dict_aux)
                        continue
                    
                    add_news = True
                    for news in self.news:
                        if dict_aux['materia'] == news['materia'] and dict_aux['fonte'] == news['fonte']:
                            add_news = False
                            break

                    if add_news:
                        self.news.insert(0, dict_aux)

            self.news = sorted(self.news, key=lambda d: d['data'], reverse=True)
            self._update_file(self.news, mode='news')
            time.sleep(10)


self = News() 
self.kill = True