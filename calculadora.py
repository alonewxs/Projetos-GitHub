

operador = input("Escolha: + - / x ")
num_1 = input("Digite o primeiro numero: ")
num_2 = input("Digite o segundo numero: ")

while True:
    try:
        num1_int = int(num_1)
        num2_int = int(num_2)

        if operador not in ["+", "-", "/", "x"]:
            print("Escolha um operador valido! ")
            break

    except ValueError:
        print("Você não inseriu um numero correto")
        break


    def resultados():
        if operador == "+":
            resultado_soma = num1_int + num2_int
            print(f"{num1_int} + {num2_int} = {resultado_soma:.2f}")
        elif operador == "-":
            resultado_menos = num1_int - num2_int
            print(f"{num1_int} - {num2_int} = {resultado_menos:.2f}")
        elif operador == "/":
            resultado_divisao = num1_int / num2_int
            print(f"{num1_int} / {num2_int} = {resultado_divisao:.0f}")
        else:
            resultado_multiplicacao = num1_int * num2_int
            print(f"{num1_int} * {num2_int} = {resultado_multiplicacao:.1f}")

    resultados()
    break

