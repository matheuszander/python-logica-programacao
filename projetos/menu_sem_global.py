def mostrar_menu():
    print('#1 - Adicionar número')
    print('#2 - Mostrar números')
    print('#3 - Somar números')
    print('#4 - Limpar lista')
    print('#5 - Sair')


def pedir_numero():
    while True:
        try:
            pedir = int(input('Escolha um número: '))
            return pedir
        except:
            print('Escolha apenas números! ')


def adicionar_numero(lista):
    guardar = pedir_numero()
    lista.append(guardar)


def obter_numeros(lista):
    return lista


def somar_numeros(lista):
    acumulador = 0
    for x in lista:
        acumulador += x
    return acumulador


def limpar_lista(lista):
    lista.clear()


numeros = []

while True:
    mostrar_menu()
    try:
        pedir_menu = int(input('Escolha uma opção: '))
    except:
        print('Apenas números, sem letras! ')
        continue

    if pedir_menu == 1:
        adicionar_numero(numeros)

    elif pedir_menu == 2:
        print(obter_numeros(numeros))

    elif pedir_menu == 3:
        print(somar_numeros(numeros))

    elif pedir_menu == 4:
        limpar_lista(numeros)
        print('Limpando lista...')

    elif pedir_menu == 5:
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida!')
