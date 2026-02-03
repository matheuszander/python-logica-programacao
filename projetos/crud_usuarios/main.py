usuarios = []


def pedir_nome():
    nome = input("Digite o nome: ")
    return nome


def pedir_idade():
    while True:
        try:
            idade = int(input("Digite a idade: "))
            return idade
        except:
            print("Use apenas números para a idade.")


def cadastrar_usuario(usuarios):
    nome = pedir_nome()
    idade = pedir_idade()

    usuario = {
        "nome": nome,
        "idade": idade
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def buscar_usuario_por_nome(usuarios, nome):
    for usuario in usuarios:
        if usuario["nome"] == nome:
            return usuario
    return None


def mostrar_usuario(usuario):
    print("Nome:", usuario["nome"])
    print("Idade:", usuario["idade"])


def editar_usuario(usuarios):
    nome_busca = input("Digite o nome do usuário que deseja editar: ")
    usuario = buscar_usuario_por_nome(usuarios, nome_busca)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    novo_nome = input("Digite o novo nome: ")
    nova_idade = pedir_idade()

    usuario["nome"] = novo_nome
    usuario["idade"] = nova_idade

    print("Usuário editado com sucesso!")


def excluir_usuario(usuarios):
    nome_busca = input("Digite o nome do usuário que deseja excluir: ")
    usuario = buscar_usuario_por_nome(usuarios, nome_busca)

    if usuario is None:
        print("Usuário não encontrado.")
        return

    usuarios.remove(usuario)
    print("Usuário removido com sucesso!")
    print("Usuários restantes:", len(usuarios))


def mostrar_menu():
    print("\n==== MENU ====")
    print("1 - Cadastrar usuário")
    print("2 - Buscar usuário")
    print("3 - Editar usuário")
    print("4 - Excluir usuário")
    print("5 - Sair")


def main():
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except:
            print("Digite apenas números.")
            continue

        if opcao == 1:
            cadastrar_usuario(usuarios)

        elif opcao == 2:
            nome_busca = input("Digite o nome que deseja buscar: ")
            usuario = buscar_usuario_por_nome(usuarios, nome_busca)

            if usuario is None:
                print("Usuário não encontrado.")
            else:
                mostrar_usuario(usuario)

        elif opcao == 3:
            editar_usuario(usuarios)

        elif opcao == 4:
            excluir_usuario(usuarios)

        elif opcao == 5:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida.")


main()
