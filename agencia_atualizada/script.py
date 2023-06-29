def depositar(deposito, saldo_conta, extrato_conta):
    deposito = deposito
    if deposito <= 0:
        print("Valor inválido, por favor realize a operação novamente!")
    else:
        saldo_conta += deposito
        extrato_conta.append(f'Deposito: R${deposito}')
        print('Deposito realizado com sucesso.')
        print(f'Saldo em conta: R${saldo_conta:.2f}')
        return saldo_conta

def sacar(*, saque, saldo, limite_saque, limite_diario, numero_saque_diario, extrato_conta):
    print(saldo)
    if saque > limite_diario:
        print('Limite de saque atingido, por favor tente novamente com um valor dentro do limite.')
    elif saque <= 0:
        print('Valor de saque invalido, tente novamente com um valor valido dentro do limite.')
    elif numero_saque_diario >= limite_saque:
        print(f'Limite de saque diario excedido, tente novamente um outro dia.! Limite de saque por dia: {limite_saque}')
    elif saque > saldo:
        print('Saldo insuficiente! Tente novamente com um novo valor!')
    else:
        saldo -= saque
        numero_saque_diario +=1
        extrato_conta.append(f'Saque: -R${saque}')
        print('Saque realizado com sucesso')
        print(f'Saldo em conta: R${saldo}')
    
        
def ver_extrato(extrato_conta):
    print('---------------------')
    print('Extrato da conta:')
    print(*extrato_conta, sep='\n')
    print('---------------------')


def criar_conta():
    pass

def criar_usuario():
    pass

def sair_conta(sair):
    sair = sair.upper()
    if sair == 'S':
        print('Encerrando operações')
        return False
    elif sair == 'N':
        print('Ecolha uma nova operação')
    else:
        print('Opção inválida')
        sair = input('Deseja realmente encerrar a operação? Digite S para sim e N para não: ')
        sair = sair.upper()
        sair_conta(sair)


def filtrar(usuarios, cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True

def criar_usuario(usuarios):
    cpf = input('Informe seu CPF (apenas numeros): ')
    usuario = filtrar(usuarios, cpf)
    
    if usuario:
        print('CPF do usuario ja cadastrado na base de dados')
        return
    
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento no seguinte formato: dd-mm-aaaa: ')
    endereco = input('Informe o seu endereço no formato(logradouro - nº - bairro - cidade/sigla do estado): ')
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})
    
    print("Usuario cadastrado com sucesso!")
    
def criar_conta(agencia, contas, numero_conta, usuarios):
    cpf = input("Informe o numero do seu CPF: ")
    usuario = filtrar(usuarios, cpf)
    
    if usuario:
        numero_conta += 1
        contas.append({'agencia':agencia, 'numero_conta': numero_conta, 'usuario': cpf})
        print("Usuario cadastrado com sucesso!")

def listar_contas(contas):
    for conta in contas:
        print(conta)

def main():
    AGENCIA = '0001'
    LIMITE_SAQUE = 3
    
    usuarios = []
    numero_conta = 0
    contas = []
    extrato_conta = []
    saldo_conta = 0
    limite_diario = 500
    numero_saque_diario = 0
    opcao = None
    operacao = True

    menu = """
    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Sair
    [5] Criar Usuário
    [6] Criar Conta
    [7] Listar Contas
    """
    while operacao != False:
        print(menu)
        opcao = int(input('Que operação deseja realizar? '))
        if opcao == 1:
            deposito = int(input('Por favor, insira o valor do seu depósito: '))
            saldo_conta = depositar(deposito, saldo_conta, extrato_conta)
        elif opcao == 2:
            saque = int(input('Por favor insira o valor do seu saque, limitado a R$500: '))
            saldo_conta = sacar(saque= saque, saldo= saldo_conta, limite_saque = LIMITE_SAQUE, limite_diario= limite_diario, numero_saque_diario = numero_saque_diario, extrato_conta = extrato_conta)
        elif opcao == 3:
          ver_extrato(extrato_conta)
        elif opcao == 4:
            sair = input('Deseja realmente encerrar a operação? Digite S para sim e N para não: ')
            sair = sair.upper()
            operacao = sair_conta(sair)
        elif opcao == 5:
            criar_usuario(usuarios)
        elif opcao == 6:
            criar_conta(agencia=AGENCIA, contas=contas, numero_conta=numero_conta, usuarios=usuarios)
        elif opcao == 7:
            listar_contas(contas)
        elif opcao > 7 or opcao < 1:
            print('Opção inválida, tente novamente.')
            
main()