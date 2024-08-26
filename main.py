import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=tempo&oq=tempo&"
#Coloque seu user agent
headers = {"user-agent": '''Your user agent!''' }

requisicao = requests.get(url, headers=headers)
site = BeautifulSoup(requisicao.text, "html.parser")

dia_hoje = site.find('div', class_="Z1VzSb")
dia_hoje = dia_hoje['aria-label']
temp_hoje = site.find('span', class_="wob_t q8U8x")
temp_hoje = temp_hoje.get_text()
clima_hoje = site.find('span', id="wob_dc")
clima_hoje = clima_hoje.get_text()

print("Estamos em uma {}, com clima {} e temperatura de {}°C".format(dia_hoje, clima_hoje, temp_hoje))

