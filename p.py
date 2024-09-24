INFORMACOES = 'Nome|Endereço|Serviço|Tipo de Veículo'
LISTA_CLIENTES = 'sprint3-python-tabela.txt'


def carregar_clientes():
    """Carrega a lista de clientes a partir do arquivo."""
    clientes = []
    try:
        with open(LISTA_CLIENTES, 'r') as file:
            linhas = file.readlines()
            # Ignorar a primeira linha do cabeçalho
            for linha in linhas[1:]:
                if linha.strip():
                    clientes.append(linha.strip())
    except FileNotFoundError:
        pass  # Se o arquivo não existir, apenas retorna uma lista vazia
    return clientes


def salvar_clientes(clientes):
    """Salva a lista de clientes no arquivo."""
    with open(LISTA_CLIENTES, 'w') as file:
        # Escrever o cabeçalho
        file.write(INFORMACOES + '\n')
        for cliente in clientes:
            file.write(cliente + '\n')


def adicionar_cliente(clientes):
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    servico = input("Serviço: ")
    tipo_veiculo = input("Tipo de Veículo: ")
    novo_cliente = f"{nome}|{endereco}|{servico}|{tipo_veiculo}"
    clientes.append(novo_cliente)
    salvar_clientes(clientes)
    print(f"Cliente {nome} adicionado com sucesso!")


def atualizar_cliente(clientes):
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return

    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. {cliente}")

    indice = int(input("Escolha o número do cliente a ser atualizado: ")) - 1
    if 0 <= indice < len(clientes):
        cliente_atualizado = clientes[indice].split('|')
        print(f"Atualizando {cliente_atualizado[0]}")
        nome = input(f"Nome ({cliente_atualizado[0]}): ") or cliente_atualizado[0]
        endereco = input(f"Endereço ({cliente_atualizado[1]}): ") or cliente_atualizado[1]
        servico = input(f"Serviço ({cliente_atualizado[2]}): ") or cliente_atualizado[2]
        tipo_veiculo = input(f"Tipo de Veículo ({cliente_atualizado[3]}): ") or cliente_atualizado[3]
        clientes[indice] = f"{nome}|{endereco}|{servico}|{tipo_veiculo}"
        salvar_clientes(clientes)
        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")


def remover_cliente(clientes):
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return

    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. {cliente}")

    indice = int(input("Escolha o número do cliente a ser removido: ")) - 1
    if 0 <= indice < len(clientes):
        cliente_removido = clientes.pop(indice)
        salvar_clientes(clientes)
        print(f"Cliente {cliente_removido.split('|')[0]} removido com sucesso!")
    else:
        print("Cliente não encontrado.")


def menu():
    clientes = carregar_clientes()
    while True:
        print("\nSistema de Gestão de Clientes")
        print("1. Adicionar cliente")
        print("2. Atualizar cliente")
        print("3. Remover cliente")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_cliente(clientes)
        elif opcao == '2':
            atualizar_cliente(clientes)
        elif opcao == '3':
            remover_cliente(clientes)
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


menu()
