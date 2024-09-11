menu = """
=============== Menu ============

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

============ Naja Bank ==========

Digite a opção desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1": # Depositar

        valor = float(input("\nInforme o valor do Déposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("\nOps! O valor informado é inválido.")

    elif opcao == "2": # Sacar

        valor = float(input("\nInforme o valor do Saque: "))

        excedeu_valor_saldo = valor > saldo
        excedeu_valor_limite = valor > limite
        excedeu_valor_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_valor_saldo:
            print("\nOps! Saldo insuficiente.")
        elif excedeu_valor_limite:
            print("\nOps! Saque excedeu o limite.")
        elif excedeu_valor_saques:
            print("\nOps! Número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("\nOps! O valor informado é inválido.")

    elif opcao == "3": # Extrato

        print("\n---------------- Info. Extrato ----------------")
        print("Não foram realizadas transações.\n" if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("-----------------------------------------------")

    elif opcao == "0": # Sair
        print("Obrigado por utilizar o Naja Bank\n")
        break
    else:
        print("\nOperação inválida, digite novamente a opção desejada.")