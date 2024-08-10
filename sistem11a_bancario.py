menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite_por_saque = 500
extrato = ""
saques_realizados = 0
LIMITE_SAQUES_DIARIOS = 3


while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe um valor para depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Valor depositado com sucesso!")

        else:
            print("Erro! O valor inserido é inválido!")

    elif opcao == 2:
        saque = float(input("Informe um valor para sacar: "))

        if saque > saldo:
            print("Erro na operação! Você não possui saldo suficiente!")

        elif saque > limite_por_saque:
            print("Erro na operação! O valor de saque excede o limite!")

        elif saques_realizados >= LIMITE_SAQUES_DIARIOS:
            print("Erro na operação! Número diário de saques atingido!")

        elif saque > 0 and saque <= saldo:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            saques_realizados += 1
            print("Saque realizado com sucesso!")

        else:
            print("Erro! Informe um valor válido!")

    elif opcao == 3:
        print("\n================Extrato================")
        print("Não houve movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao == 0:
        break

    else:
        print("Erro! Por favor, selecione novamente a operação desejada!")


            
