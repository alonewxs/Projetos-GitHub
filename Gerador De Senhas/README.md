## Gerador de Senhas Aleatorias

Gerador de senhas aleatórias rodando no terminal, feito totalmente em Python. Conta com sistema de login e registro de usuários com persistência de dados.
Funcionalidades

- Sistema de login e registro de usuários
- Dados salvos em arquivo JSON (persistem ao fechar o terminal)
- Gera senhas com o número de caracteres escolhido pelo usuário (mínimo 5)
- Opção de incluir números na senha
- Validação de entradas inválidas
- Animação de loading durante a geração



## Funcionalidades

- Gera senhas com o número de caracteres escolhido pelo usuário
- Opção de incluir números na senha
- Validação de entradas inválidas
- Animação de loading durante a geração
- Guarda informações do login no .json
- Sistema de verificação no login



## Como Usar

1. Execute o arquivo `gerador.py`
2. Escolha entre `Login` ou `Registro`

3. `Registro:` crie um username e senha para sua conta
4. `Login:` acesse com seu username e senha cadastrados

5. Informe a quantidade de caracteres desejada (mínimo 5)
6. Escolha se deseja números na senha (S/N)
7. Aguarde a animação e copie sua senha gerada



## Execução do Codigo

```
-----------------------------------------------------------
---- Seja bem vindo(a) ao sistema de gerador de Senhas ----
-----------------------------------------------------------
```

## Caso de Registro

[1] Login
[2] Registro: 2

Escolha o seu username: dev supremo
Escolha sua senha: senhadevbom

## Caso de Login

[1] Login
[2] Registro: 1

## Exemplo

Qual seu user? dev supremo
Qual sua senha? senhadevbom
Seja bem vindo(a) dev supremo!

Quantos caracteres? Minimo de 5: 10
Deseja numeros na senha? S/N: s
Gerando sua senha... 🔐
Sua senha gerada foi: `aB3xK9mQpL`



## Estrutura dos Arquivos
├── gerador.py       # código principal
└── contas.json      # contas salvas (gerado automaticamente)



## Tecnologias
`Python 3`
Bibliotecas: `random`, `string`, `time`, `json`, `os`