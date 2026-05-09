import requests
import time
import os
from dotenv import load_dotenv


load_dotenv()


lista = {
    "1": {"sigla": "EUR", "nome": "Euro"},
    "2": {"sigla": "BRL", "nome": "Real Brasileiro"},
    "3": {"sigla": "CHF", "nome": "Franco Suíço"},
    "4": {"sigla": "JPY", "nome": "Iene Japonês"},
    "5": {"sigla": "GBP", "nome": "Libra Esterlina"},
    "6": {"sigla": "CNY", "nome": "Yuan Chinês"},
    "7": {"sigla": "USD", "nome": "Dólar Americano"},
    "8": {"sigla": "AED", "nome": "Dirham dos Emirados"},
    "9": {"sigla": "AUD", "nome": "Dólar Australiano"},
}

os.system("cls")

for num, dados in lista.items(): ## enumera e mostra o nome de cada moeda
    print(f"[{num}] {dados['sigla']} - {dados['nome']}")

moeda_base = input("Qual moeda base você deseja utilizar? Escolha um numero:")
moeda_convertida = input("Qual moeda que você deseja ver quanto ficara? Escolha um numero:")

if moeda_base in lista and moeda_convertida in lista: ## verifica se a resposta da pergunta existe na lista
    moeda = lista[moeda_base]["sigla"] ## moeda base
    moeda2 = lista[moeda_convertida]["sigla"] ## moeda convertida


    API_KEY = os.getenv("API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{moeda}"


    response = requests.get(url)
    data = response.json()

    pergunta_3 = float(input(f"Digite a quantidade de {moeda} que quer converter para {moeda2}: "))


    conversao = data["conversion_rates"][moeda2] ## isso pega a taxa de conversão de acordo com a URL
    convertido = conversao * pergunta_3


    os.system("cls")

    print(f"Você escolheu converter {moeda} para {moeda2}")

    os.system("cls")

    print("Convertendo...")

    time.sleep(1)

    os.system("cls")

    print(f"{pergunta_3:.2f} {moeda} = {convertido:.2f} {moeda2}")
else:
    print("Opção escolhida esta invalida!")