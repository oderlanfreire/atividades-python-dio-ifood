# Variaveis
saldo_conta = 0
extrato_conta = []
limite_diario = 500
numero_saque_diario = 0
opcao = None
LIMITE_SAQUE = 3
operacao = True

menu = """[1] Deposito\n
[2] Saque\n
[3] Extrato\n
[4] Sair
 """

#Lógica
while operacao != False:
    print(menu)
    opcao = int(input('Que operação deseja realizar? '))
    if opcao == 1:
        deposito = int(input('Por favor, insira o valor do seu depósito: '))
        if deposito <= 0:
            print("Valor inválido, por favor realize a operação novamente!")
        else:
            saldo_conta = deposito
            extrato_conta.append(f'Deposito: R${deposito}')
            print('Deposito realizado com sucesso.')
            print(f'Saldo em conta: R${saldo_conta:.2f}')
    if opcao == 2:
        saque = int(input('Por favor insira o valor do seu saque, limitado a R$500: '))
        if saque > 500:
            print('Limite de saque atingido, por favor tente novamente com um valor dentro do limite.')
        elif saque <= 0:
            print('Valor de saque invalido, tente novamente com um valor valido dentro do limite.')
        elif numero_saque_diario >= LIMITE_SAQUE:
            print(f'Limite de saque diario excedido, tente novamente um outro dia.! Limite de saque por dia: {LIMITE_SAQUE}')
        elif saque > saldo_conta:
            print('Saldo insuficiente! Tente novamente com um novo valor!')
        else:
            saldo_conta -= saque
            numero_saque_diario +=1
            extrato_conta.append(f'Saque: -R${saque}')
            print('Saque realizado com sucesso')
            print(f'Saldo em conta: R${saldo_conta}')
    if opcao == 3:
        print('---------------------')
        print('Extrato da conta:')
        print(*extrato_conta, sep='\n')
        print('---------------------')
    if opcao == 4:
        sair = input('Deseja realmente encerrar a operação? Digite S para sim e N para não: ')
        sair.upper()
        if sair == 'S':
            print('Encerrando operações')
            operacao = False
    else:
        print('Opção inválida, tente novamente.')