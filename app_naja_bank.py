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

    if opcao == "1":
        print("opcao 1 - depositar")
    elif opcao == "2":
        print("opcao 2 - sacar")
    elif opcao == "3":
        print("opcao 3 - extrato")
    elif opcao == "0":
        print("opcao 0 - sair")
        break
    else:
        print("\nOperação inválida, digite novamente a opção desejada.")