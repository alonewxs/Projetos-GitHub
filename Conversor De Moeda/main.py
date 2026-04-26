import requests
import time
import os
from dotenv import load_dotenv


load_dotenv()


lista = {
    "1": "EUR",
    "2": "BRL",
    "3": "CHF",
    "4": "JPY",
    "5": "GBP",
    "6": "CNY",
}


os.system("cls")


for num, nome in lista.items(): ## enumera e mostra o nome de cada moeda
    print(f"[{num}] {nome}")

moeda_base = input("Qual moeda base você deseja utilizar? Escolha um numero:  ")
moeda_convertida = input("Qual moeda que você deseja ver quanto ficara? Escolha um numero:  ")
# pergunta = input("Escolha um numero de acordo com a moeda que deseja converter: ") ## vai selecionar alguma da lista pra dar o resultado

if moeda_base in lista: ## verifica se a resposta da pergunta existe na lista
    moeda = lista[moeda_base] ## moeda base
    moeda2 = lista[moeda_convertida] ## moeda convertida


    API_KEY = os.getenv("API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{moeda}"


    response = requests.get(url)
    data = response.json()

    pergunta_3 = float(input(f"Digite a quantidade de {moeda} que quer converter para {moeda2}: "))


    conversao = data["conversion_rates"][moeda2] ## isso pega a taxa de conversão de acordo com a URL
    convertido = conversao * pergunta_3
    # moeda_taxa = convertido / conversao


    os.system("cls")

    print(f"Você escolheu converter {moeda} para {moeda2}")

    os.system("cls")

    print("Convertendo...")
    
    time.sleep(1)

    os.system("cls")

    print(f"{pergunta_3:.2f} {moeda} = {convertido:.2f} {moeda2}")
else:
    print("Opção escolhida invalida!")