# Valorant Tracker

Um script simples em Python que consulta informações de rank de um jogador de Valorant usando uma API externa.

Ele mostra os dados citados abaixo:

* Rank atual
* Maior rank ( Peak Rank )
* MMR atual
* MMR da última partida

---

## Sobre o projeto

Esse projeto foi feito com o objetivo de praticar:

* Consumo de APIs REST
* Manipulação de JSON
* Uso de variáveis de ambiente ( .env )
* Organização de código simples e funcional

---

## Como funciona

O script pede algumas informações no terminal:

* `Região` ( ex: BR, NA, EU... )
* `Nome do jogador` ( ex: TenZ )
* `Tag` ( ex: BR1, NA1... )

Depois disso, ele faz uma requisição para a API e retorna os dados formatados na tela.

---

## Tecnologias usadas

* Python
* requests
* python-dotenv

---

## Onde pegar a API Key?

Você pode obter sua API Key na API do HenrikDev.
Link: `https://api.henrikdev.xyz/dashboard/`

---

## Como usar

Clone o repositório e execute:

python main.py

Depois responda as perguntas:

Região ( BR, NA, EU, AP, KR )
Nome do jogador: 
Tag do jogador: 

---

## Exemplo de OutPut

`Usuario:` TenZ#NA1
`Rank Atual:` Radiante
`Peak Rank:` Radiante
`MMR Ultimo Jogo:` +25
`MMR Atual:` 90

---

## Estrutura do projeto

Tracker-Valorant/
│── `main.py`
│── `.env`
└── `README.md`

---