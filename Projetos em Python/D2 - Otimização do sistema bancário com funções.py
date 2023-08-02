def menu():
    menu_text = '''
    Bem vindo(a) ao Sistema Bancário!
    Assinale abaixo a operação que deseja realizar:
    [1] Depositar
    [2] Sacar
    [3] Ver extrato
    [4] Novo usuário
    [5] Criar conta
    [6] Listar contas
    [7] Sair
    '''
    return int(input(menu_text))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito de R$ {valor:.2f}")
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nValor inválido para depósito.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, qtde_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = qtde_saque >= limite_saque

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excedeu o limite")
    elif excedeu_saques:
        print("Operação falhou! Número de saques excedido")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        qtde_saque += 1
        print("\nSaque realizado com sucesso")
    else:
        print("\nOperação falhou! O valor informado é inválido")

    return saldo, extrato

def imprimir_extrato(saldo, /, *,  extrato):
    print("\nExtrato:")
    if not extrato:
        print("Não houve movimentações")
    else:
        for registro in extrato:
            print(registro)
    print(f"\nSaldo: \tR$ {saldo:.2f}")
    

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = encontrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF")
        return

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe seu endereço [logradouro, número, bairro, cidade/estado]: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def encontrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = encontrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n[ERRO] Usuário não encontrado. Processo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f'''
        Agência:\t{conta['agencia']}
        N°:\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        '''
        print("-" * 100)
        print(linha)

def main():
    saldo = 0
    extrato = []
    qtde_saque = 0
    SAQUE_LIMITE = 500
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor que você deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=SAQUE_LIMITE,
                qtde_saque=qtde_saque,
                limite_saque=LIMITE_SAQUES,  
            )

        elif opcao == 3:
            imprimir_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)
        

        elif opcao == 7:
            break

        else:
            print("Operação inválida. Selecione novamente a operação desejada")


main()
