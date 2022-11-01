from pyautogui import sleep
import requests
from bs4 import BeautifulSoup
import shutil

url = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

for link in links:
	if ('.pdf' in link.get('href', []) or '.xlsx' in link.get('href', [])):
            if("Anexo" in link.string):
                response = requests.get(link.get('href'))

                pdf = open(link.string.strip() + "." +link.get('href').strip().split('.')[-1], 'wb')
                pdf.write(response.content)
                pdf.close()
                print("File ", link.string, " downloaded")

            if("Anexo" not in link.string):
                print("File ", link.string, "it's not an attachment")

print("All files with attachement downloaded")