
# Sistema Bancário - Naja Bank

Este projeto simula um sistema bancário simples abordando menu interativo e estruturas de repetições utilizando Python.

Tópicos abordados durante o desenvolvimento do Naja Bank:

- Criação de menu **visível** em prompt de comando;
- Estrutura de repetições **while**, **if**, **else** e **elif**;
- Formatação de **strings** e **valores**.

## Menu
- Depositar;
- Sacar;
- Extrato;
- Sair.

```python
=============== Menu ============

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

============ Naja Bank ==========
```
## Funcionalidades

### 1. Depositar

-   Solicita ao usuário o valor do depósito.
-   Adiciona o valor ao saldo se for positivo.
-   Registra a transação no extrato.
```python
[...]
if  opcao  ==  "1": # Depositar
	valor  =  float(input("\nInforme o valor do Déposito: "))
		
	if  valor  >  0:
		saldo  +=  valor
		extrato  +=  f"Depósito: R${valor:.2f}\n"
	else:
		print("\nOps! O valor informado é inválido.")
[...]
```

### 2. Sacar

-   Solicita ao usuário o valor do saque.
-   Verifica se o valor do saque não excede o saldo, o limite ou o número máximo de saques permitidos.
-   Deduz o valor do saldo se todas as condições forem atendidas.
-   Registra a transação no extrato.
```python
[...]
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
[...]
```

### 3. Extrato

-   Exibe todas as transações realizadas.
-   Mostra o saldo atual.
```python
[...]
elif opcao == "3": # Extrato

        print("\n---------------- Info. Extrato ----------------")
        print("Não foram realizadas transações.\n" if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("-----------------------------------------------")
[...]
```
### 0. Sair

-   Encerra o programa.
```python
[...]
elif opcao == "0": # Sair
        print("Obrigado por utilizar o Naja Bank\n")
        break
    else:
        print("\nOperação inválida, digite novamente a opção desejada.")
[...]
```

## Regras de Negócio

-   O limite de saque é de R$500,00.
-   O número máximo de saques diários é 3.
-   Não são permitidos depósitos ou saques de valores negativos.