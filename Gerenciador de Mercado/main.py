############################
## Objeivo: Criar mercado ##
############################

from rich.table import Table
from rich.console import Console
from rich import print
from rich.progress import track
import json
import time
import builtins
import os


ESTOQUE = os.path.join(os.path.dirname(__file__), "estoque.json")


# =============== SO SOBRE O ARQUIVO EM JSON ====================== #

def carregar_dados(): 
    if os.path.exists(ESTOQUE):
        with open(ESTOQUE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_dados(dados):
    with open(ESTOQUE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# ================================================================= #



# ========================= ADD/REM PRODUTOS ========================== #

def adicionar_produto(estoque):
    nome = input("Nome do produto: ").lower().strip()
    preco = input("Preço: ")
    quantidade = input("Quantidade: ")


    while True:
        try:
            preco_float = float(preco.replace(",", "."))
            break
        except ValueError:
            print("Digite um número valido, EX: 52.00")
            continue
    while True:
        try:
            quantidade_int = int(quantidade)
            break
        except ValueError:
            print("Digite um numero para estoque valido, EX: 5")


    for i in estoque:
        if nome == i["nome"]:
            i["quantidade"] += quantidade_int
            salvar_dados(estoque)
            print("Nome repetido identificado, adicionei a quantidade ")
            return

    produto = {
        "nome": nome,
        "preco": preco_float,
        "quantidade": quantidade_int
    }


    estoque.append(produto) ## vai ".append" o q a pessoa digitou no produto
    salvar_dados(estoque) ## isso aq vai salvar la no .json
    print("Produto adicionado com sucesso!")


def remover_produto(estoque):
    nome = input("Nome do produto: ").lower().strip()
    quantidade = int(input("Quantidade: "))

    for i in estoque:
        if nome == i["nome"]:
            if quantidade > i["quantidade"]:
                print(f"Estoque insuficiente! Temos apenas {i['quantidade']} unidades.")
                return
            i["quantidade"] -= quantidade ## isso ate o return é do 1 if por isso funciona
            salvar_dados(estoque)
            print("Quantidade removida do estoque com sucesso!")
            return

    print("Produto não encontrado no estoque.")

# ===================================================================== #



# ======================== LISTA PRODUTOS ========================= #

def listar_produtos(estoque):
    if not estoque:
        print("Este produto não esta em estoque. Caso seja um manager adicione o produto no estoque para vender!!")
        return

    os.system("cls")

    console = Console()
    tabela = Table(title="📦 Estoque")

    tabela.add_column("ID", style="white")
    tabela.add_column("Produto", style="cyan")
    tabela.add_column("Preço", style="green")
    tabela.add_column("Qtd", style="magenta")

    for i, p in enumerate(estoque, 1):
        tabela.add_row(
            str(i),
            p["nome"].capitalize(),
            f"R${p['preco']:.2f}",
            str(p["quantidade"])
        )

    console.print(tabela)

# ================================================================= #

def menu():
    estoque = carregar_dados()

    while True:
        print("\n[bold cyan]==== MERCADO ====")
        print("[bold green]1 - Adicionar produto")
        print("[bold blue]2 - Listar produtos")
        print("[bold red]3 - Remover produto")
        print("[bold gray]4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_produto(estoque)

        elif opcao == "2":
            listar_produtos(estoque)

        elif opcao == "3":
            remover_produto(estoque)

        elif opcao == "4":
            print("Saindo...")
            time.sleep(1.2)
            os.system("cls")
            break

        else:
            print("[red]Opção inválida![/]")

menu()