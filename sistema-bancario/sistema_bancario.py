import os
lines = os.get_terminal_size().lines

# Input da tela de menu:

menu = """
Selecione a opção desejada:   |
                              |
[s] -> Para Saque.            |
[d] -> Para Depositos.        |
[e] -> Para Extratos.         |
                              |
[q] -> Para Sair.             |
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ .

"""

# Declaracao de variaveis

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

valor_total = 0

while True: 
    opcao = input(menu)

    if opcao == "d":
        print("\n"*lines)

        valor = float(input("Digite o valor do deposito:"))

        if valor > 0:
            saldo += valor
            extrato += f"\n++Deposito de R${valor:.2f}\n"
            print("\n")
            print(f"\nR${valor:.2f} adicionado a sua conta.")
            print(f"\n\nSaldo total: R${saldo:.2f}")
        else:
            print("Operação não realizada, o valor informado é invalido.")
    
    elif opcao == "s":
        print("\n"*lines)
        
        valor = float(input("Digite o valor do saque: "))

        saldo_insuficiente = valor > saldo
        excedeu_limite_de_saque = valor > limite
        excedeu_numero_de_saque = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("\nOperação não realizada, saldo insuficiente.")
        
        elif excedeu_limite_de_saque:
            print(f"\nOperação não realizada, você solicitou o valor de R${valor}")
            print(f"\nPor segurança você tem um limite de R${limite:.2f} por operação.")
        elif excedeu_numero_de_saque:
            print("\nLimite diario de saques excedido.")
        
        elif valor > 0 and valor <= saldo:
            saldo -= valor
            print("\n"*lines)
            extrato += f"\n--Saque de R${valor:.2f}\n"
            print(f"Saldo total: R${saldo:.2f}")
            numero_saques += 1
        
        else:
            print("\nOperação falhou, valor informado é invalido.")
    
    elif opcao == "e": 
        if extrato != "":
            print("\n"*lines)
            print("-" * 30)
            print("Extrato:")
            print(extrato)
            print(f"\nSaldo: R${saldo:.2f}")
        else:
            print("\n"*lines)
            print("\nNenhuma movimentação foi realizada.\n")
    
    elif opcao =="q":
        break
    
    else: print("Operação invalida, por favor verifique se a opção desejada esta correta.")