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

USER_GERENTE = "Admin"
SENHA_GERENTE = "Admin54321"

CODIGO_FUNCIONARIO = "554221"

USER_REGISTRO = ""
SENHA_REGISTRO = ""

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
        print("Não tem produto em estoque. Caso seja um Gerente adicione o produto no estoque para vender!!")
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


# ========================= LOGIN ( FUNCIONARIO OU CLIENTE ) PRODUTOS ========================== #

cargo = input("Deseja entra como? \n[1] Gerente \n[2] Cliente\n")

ask_user = ""

try:
    cargo = int(cargo)
except ValueError:
    print("Digite apenas, 1 ou 2") 

if cargo == 1:
    os.system("cls")
    print("Seja bem vindo(a) ao painel de Login Administrativo")
    time.sleep(0.5)
    print("Faça Login/Registo")
    print("\n[1] Login \n[2] Registro\n")
    ask_user = input("")

    login_regist = ask_user

elif cargo == 2:
    os.system("cls")
    menu()
    
while True:
    if login_regist == "1":
        user = input("Qual Usuario: ")
        senha = input("Qual Senha: ")

        if user == USER_GERENTE and senha == SENHA_GERENTE:
            print("Login feito com Sucesso!!")
            os.system("cls")
            break
        else:
            print("Usuario ou Senha incorreto!!")
            os.system("cls")
            continue
    else:
        os.system("cls")
        ask_codigo = input("Qual codigo de Funcionario? ")
        if ask_codigo == CODIGO_FUNCIONARIO:
            USER_REGISTRO = input("Qual Usuario para Registro? ")
            SENHA_REGISTRO = input("Qual Senha para Registro? ")
            os.system("cls")
            time.sleep(1)
            print("Usuario Cadstrado")
        else:
            print("Codigo de Funcionario incorreto!")
            continue
        break
        

menu()
           