clientes = []
n_clientes = 1

def menu() :
    option = int(input('''
[1] - Cadastrar cliente
[2] - Consultar Clientes
[3] - Editar Cliente
[4] - Sair do programa
'''))

    return option

def cadastra_cliente() :
    cliente_nome = input('Digite o nome do cliente: ')
    cliente_cep = input('Digite o cep do cliente: ')
    cliente_telefone = input('Digite o telefone do cliente: ')
    clientes_dados = (cliente_nome,cliente_cep,cliente_telefone)
    clientes.append(clientes_dados)
    print(clientes)
    print('Cliente adicionado')

def mostrar_cliente() :
    print(f'''
    Nome: {clientes[0]}
    Cep: {clientes[1]}
    Telefone: {Clientes[2]}''')


def programa() :

    option = menu()
    while True:
        if option == 1 :
            cadastra_cliente()
        if option == 2 :
            mostrar_cliente()
programa()


