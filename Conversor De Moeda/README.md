# Conversor de Moedas

Um sistema simples de conversão de moedas feito 100% em Python, rodando no terminal, utilizando uma API externa para obter taxas de câmbio em tempo real.

---

## Sobre o projeto

Este projeto permite converter valores entre diferentes moedas listadas

Ele funciona assim:

- Escolha a moeda base
- Escolha a moeda para conversão
- Digite o valor
- Receba o resultado instantaneamente

Sempre usando os dados da API da `exchangerate-api`

---

### Funcionalidades ###

### Conversão de Moedas

* Conversão em tempo real
* Suporte a múltiplas moedas
* Cálculo automático baseado na taxa atual

### Interação no Terminal

* Menu simples e intuitivo
* Seleção de moedas por número
* Exibição limpa do resultado

### Integração com API

* Uso da ExchangeRate API
* Dados atualizados automaticamente
* Conversões precisas

---

## Moedas disponíveis

* `EUR` (Euro)
* `BRL` (Real Brasileiro)
* `CHF` (Franco Suíço)
* `JPY` (Iene Japonês)
* `GBP` (Libra Esterlina)
* `CNY` (Yuan Chinês)

---

## Tecnologias utilizadas

* Python (100%)
* Biblioteca `requests` (requisições HTTP)
* Biblioteca `python-dotenv` (variáveis de ambiente)
* API ExchangeRate

---

## Estrutura
`📁 projeto/`
`├── main.py`
`├── .env`

---

## Interface (Terminal)
[1] EUR
[2] BRL
[3] CHF
[4] JPY
[5] GBP
[6] CNY

---

## Exemplo de uso

### Conversão

* Moeda base: EUR
* Moeda convertida: BRL
* Valor: 10

### Resultado

10.00 EUR = 54.32 BRL

---

## ⚙️ Configuração

Antes de rodar o projeto, você precisa criar um arquivo `.env` com sua chave da API:
API_KEY=sua_chave_aqui

Você pode obter sua chave gratuita em:
`https://www.exchangerate-api.com/`
