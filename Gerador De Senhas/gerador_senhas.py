import random
import time
import string
import json
import os


emojis = ["🔒", "🔑", "⚙️", "🔐", "🛡️"]
ARQUIVO = "contas.json"


def carregar_contas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []  ## se o arquivo não existir começa vazio

def salvar_contas(contas):
    with open(ARQUIVO, "w") as f:
        json.dump(contas, f, indent=4)


contas = carregar_contas()


print("-----------------------------------------------------------")
print("---- Seja bem vindo(a) ao sistema de gerador de Senhas ----")
print("-----------------------------------------------------------")
time.sleep(2)

###### LOGIN ######

while True:
    resposta_user = int(input("[1] Login \n[2] Registro "))
    
    if resposta_user == 2:
        user_registro = str(input("Escolha o seu username: ")).lower()
        senha_registro = input("Escolha sua senha: ")
        
        user_existe = any( conta["user"] and conta["senha"] == user_registro for conta in contas )
        
        
        if user_existe:
            print("Você ja tem um cadastro")
            continue
        else:
            contas.append({"user": user_registro, "senha": senha_registro})
            salvar_contas(contas)
            break
    
    elif resposta_user == 1:
        user_login = input("Qual seu user? ").lower()
        senha_login = input("Qual sua senha? ")
        
        conta_encontrada = any(
        conta["user"] == user_login and conta["senha"] == senha_login
        for conta in contas
        )
        
        if conta_encontrada:
            print(f"Seja bem vindo(a) {user_login}!")
            break
        else:
            print("Usuario ou Senha incorreto!")
            continue
    

caracteres = int(input("Primeiro, deseja gerar uma chave com quantos caracteres? Minimo de 5 Caracteres: "))
time.sleep(0.5)
numeros = str(input("Deseja que tenha numeros na senha? S/N: ").lower())
time.sleep(1)


try:

    caracteres_int = int(caracteres)  ## faz a verificação
    numeros_str = str(numeros) ## verify tb

    if caracteres_int < 5:
        print("A senha deve ter no mínimo 5 Caracteres! ") ## se as caracteres tiver - doq 5 ele n valida
        
    if numeros not in ["s", "n", "sim", "não", "não"]: ## coloquei opções a mais caso o usuario não leia atentamente 
        print("A resposta deve ser S ou N")

except ValueError:
    print("Numero ou Caracteres invalidos!")



inicio = time.time() 
while time.time() - inicio < 3: ## isso é so p parar qnd de 3 segundos que ai vai gerar a senha
    for x in emojis:
        print(f"\rGerando sua senha... {x}", end = "", flush = True)
        time.sleep(0.2)


letras = string.ascii_letters
num = string.digits


if numeros in ["s", "sim"]:
    senha_gerada = letras + num
else:
    senha_gerada = letras


senha = ""
for x in range(caracteres_int):
    senha += random.choice(senha_gerada)

print(f"\nSua senha gerada foi: {senha}")