# deposito: valores positivos e devem ser apresentados no extrato
# saque: 3 saques diários com limite maximo de 500 por saque. Caso nao tenha saldo deve exibir uma mensagem. Devem ser apresentados no extrato
# extrato: listar depositos, saques e saldo atual da conta. R$ 1,500.45

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo
    global extrato

    if valor < 0:
        print("O Valor do depósito não pode ser negativo!")
    else:
        saldo += valor
        extrato = extrato + f"+ R$ {valor:.2f}\n"
        print("Depósito realizado!")

def sacar(valor):
    global saldo
    global extrato
    global LIMITE_SAQUES
    global numero_saques

    if LIMITE_SAQUES < numero_saques:
        print("Limite de saques diários excecido!")
    elif valor > 500:
        print("O valor limite por saque foi execido!")
    elif saldo < valor:
        print("Saldo insuficiente para valor de saque solicitado")
    else:
        saldo -= valor
        numero_saques += 1
        LIMITE_SAQUES -= 1
        extrato +=  f"- R$ {valor:.2f}\n"
        print("Saque realizado!")

def exibir_extrato():
    global saldo

    if extrato:
        print(extrato)
        print(f"Saldo atual: {saldo} ")
    else:
        print("Não foram realizadas movimentações.")

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Digite o valor do deposito: "))
        depositar(valor)

    elif opcao == "s":
        print("Saque")
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
    
    elif opcao == "e":
        print("Extrato")
        exibir_extrato()
    elif opcao == "q":
        break
    else:
        print("Opção inválida, por favor serlecione novamente a opção desejada.")