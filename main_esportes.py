from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Modo headless
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--ignore-certificate-errors")

# Forçar a atualização do ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acesse a página de futebol
driver.get("https://www.sofascore.com/pt/futebol")

# Encontrar os links dos times
time_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/time/futebol/')]")

# Extrair os links
team_urls = [link.get_attribute('href') for link in time_links]

# Imprimir as URLs encontradas
for url in team_urls:
    print(url)

# Fechar o navegador
driver.quit()
