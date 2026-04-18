# Sistema de Mercado (CLI em Python)

Um sistema simples de gerenciamento de estoque feito 100% em Python, rodando no terminal, com interface melhorada usando **Rich**.

---

## Sobre o projeto

Este projeto simula um pequeno sistema de mercado, permitindo:

* 📦 Adicionar produtos ao estoque
* 📉 Remover produtos (baixa no estoque)
* 📊 Visualizar produtos em formato de tabela
* 💾 Salvar automaticamente os dados em um arquivo JSON

Tudo isso diretamente no terminal, sem necessidade de interface gráfica.

---

### Funcionalidades ###


### Gerenciamento de Produtos

* Adicionar novos produtos
* Evitar duplicação (soma quantidade se já existir)
* Remover quantidade de produtos existentes

### Visualização

* Tabela organizada no terminal
* ID automático para cada produto
* Preço formatado (R$)

### Persistência de Dados

* Dados salvos automaticamente em `estoque.json`
* Carregamento automático ao iniciar o sistema

---

## Tecnologias utilizadas

* Python (100%)
* JSON (armazenamento de dados)
* Biblioteca `rich` (interface no terminal)

---

## 📂 Estrutura

```
📁 projeto/
 ├── main.py
 ├── estoque.json
```

## Interface (Terminal)

```
==== MERCADO ====
1 - Adicionar produto
2 - Listar produtos
3 - Remover produto
4 - Sair
```

---

## Exemplo de uso

### ➕ Adicionar produto

* Nome: arroz
* Preço: 20.50
* Quantidade: 10

### ➖ Remover produto

* Nome: arroz
* Quantidade: 2

### Estoque

┃ ID ┃ Produto ┃ Preço ┃ Qtd ┃
  1    Arroz     20.50   8


---