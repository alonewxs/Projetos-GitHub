import random
import time
import string


emojis = ["🔒", "🔑", "⚙️", "🔐", "🛡️"]



print("-----------------------------------------------------------")
print("---- Seja bem vindo(a) ao sistema de gerador de Senhas ----")
print("-----------------------------------------------------------")
time.sleep(2)


caracteres = int(input("Primeiro, deseja gerar uma chave com quantos caracteres? Minimo de 5 Caracteres: "))
time.sleep(0.5)
numeros = input("Deseja que tenha numeros na senha? S/N: ").lower()
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