# separar as operações em funções
# saque: receber argumentos apenas por nome (saque=saque, valor=valor, limite=limite, numero_saques=numero_saques, limites_saques=limites_saques)
#   sugestao de retorno:  saldo e extrato
# depósito: receber argumentos por posicao (saldo, valor, extrato)
#   sugestao de retorno: saldo e extrato
# extrato: receber os argumentos por posicao (saldo=saldo) e nomeados (extrato)
# criar usuário (chave valor): armazenar os usuários em uma lista.
# usuario: nome, data de nascimento, cpf(numeros e único) e endereco
# endereco (string): logradouro, nro - bairro - cidade/sigla estado
# criar conta corrente, vinculando com usuario:
# amarzenar conta em uma lista
# conta: agencia(fixo "0001"), número da conta(sequencial iniciando em 1) e usuario
# usuario pode ter mais de uma conta, mas uma conta pertence somente a um usuário
# dica: para vincular um usuario a uma conta, filtre a lista de usuários buscando o numero do cpf informado para cada usuario da lista

import textwrap

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limites_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limites_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):

    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
     print("Já existe um usuário com esse CPF")
     return

    nome = input("Informe o nome do usuario: ")
    data_nascimento = input("Informe a data de Nascimento: dd-mm-aaaa ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def menu():

    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """

    return input(textwrap.dedent(menu))




def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor,extrato=extrato, limite=limite, numero_saques=numero_saques, limites_saques=limite_saques )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()