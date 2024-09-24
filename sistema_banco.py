menu = """
Escolha a opção:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_informado = float(input("Digite o valor do depósito: "))
        if valor_informado > 0:
            saldo += valor_informado
            extrato += f"Depósito: R$ {valor_informado:.2f}\n"
        else:
            print("Valor informado é inválido.")    

    elif opcao == "2":
        valor_informado = float(input("Digite o valor do saque: "))
        if valor_informado > saldo:
            print("Valor informado é superior ao saldo da conta.")
        elif valor_informado > limite:
            print("Valor informado é superior ao limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Quantidade de saques excedido.")
        elif valor_informado > 0:
            saldo -= valor_informado
            extrato += f"Saque: R$ {valor_informado:.2f}\n"
            numero_saques += 1
        else:
            print("Valor informado é inválido.")

    elif opcao == "3":
        print("\n=-=-=-=-=-=-= Extrato =-=-=-=-=-=-=")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    elif opcao == "0":
        break

    else:
        print("\nOpção inválida.")