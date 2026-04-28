import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")

os.system("cls")
print("==== SEJA BEM VINDO(A) AO PAINEL DE NOTICIAS ===")
time.sleep(1)


q = input("Escolha uma materia que deseja: ").lower()

response = requests.get(
    'https://newsapi.org/v2/everything',
    params={'q': q, 'apiKey': API_KEY}
)

data = response.json()

base = data["articles"]

os.system("cls")

if base == []:
    print(f"Não encontrei nenhuma materia com o tema: {q}")
else:
  for j, i in enumerate(base[:5]):
      print("---------")
      print(f"Notícia {j + 1}")
      print("---------")
      print(f"Autor: {i['author'] or 'Autor Desconhecido'}")
      print(f"Emissora: {i['source']['name']}")
      print(f"Link URL: {i['url']}")
      print("---------")

  time.sleep(2)

  detalhes_news = input("Deseja ver a descrição da noticia? S / N ").lower()

  while True:
      try:
          if detalhes_news == "s":
              news_desc = int(input("Qual noticia deseja ver a descrição? Digite o numero da noticia: "))

              if 1 <= news_desc <= 5:
                  print(base[news_desc - 1]["description"] or "Descrição não disponivel")
                  break
              else:
                  print("Digite um número entre 1 e 5")
                  continue

          elif detalhes_news == "n":
              print("Saindo...")
              time.sleep(0.5)
              break

          else:
              print("Digite apenas S ou N")
              detalhes_news = input("Deseja ver a descrição da noticia? S / N ").lower()

      except ValueError:
          print("Digite apenas números!")
          continue