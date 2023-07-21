saque = 0
deposito = 0
extrato = 0
saldo = 0
count = 0
SAQUE_LIMITE = 500

while True:
    menu = f'''
Bem vindo(a) ao Sistema Bancário!
Assinale abaixo a operação que deseja realizar:
[1] Depósito: Realizar depósito na sua conta.
[2] Saque: Retirar fundos da sua conta.
[3] Extrato: Verifique todas as transações realizadas em sua conta.
[4] Sair
    '''
    print(menu)
    opcao = int(input())

    if opcao == 1:
        valor1 = float(input("Informe o valor que você deseja depositar: \n"))
        deposito += valor1
        saldo += valor1
        extrato += 1

    elif opcao == 2:
        if count < 4:
            count += 1
            valor2 = float(input("Informe o valor que você deseja sacar: \n"))

            if valor2 <= saldo:
                if valor2 <= SAQUE_LIMITE:
                    saque += valor2
                    saldo -= valor2
                    extrato += 1
                else:
                    print("O valor do saque excede o limite diário!")
            else:
                print(f"Erro no saque! O valor solicitado para sacar é de {valor2}, porém o saldo consta {saldo}")
        else:
            print("O sistema deve permitir realizar 3 saques diários!")

    elif opcao == 3:
        if extrato > 0:
            print(f"Você realizou {extrato} movimentações. Segue os valores: \n")
            print(f"Depósito: R$ {deposito:.2f}. \nSaque: R$ {saque:.2f} \nSaldo: R$ {saldo:.2f}")

    elif opcao == 4:
        print("Saindo...")
        break
    else: 
        print("Erro na operação!")