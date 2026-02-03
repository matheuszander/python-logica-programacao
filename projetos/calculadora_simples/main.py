def mostrar_menu():
    print('#1 - Somar')
    print('#2 - Subtrair')
    print('#3 - Multiplicar')
    print('#4 - Dividir')
    print('#5 - Sair')

def pedir_numero():
    try:
        numero = int(input('Digite um número: '))
        return numero
    except:
        print('Use apenas números para escolher. Sem letras!')

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def mult(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        print('Não tem como dividir um número por zero!!! ')
        return None
    else:
        return a / b
    
while True:
    mostrar_menu()
    try:
        opcao = int(input('Escolha uma opção: '))
    except:
        print('Use apenas números para escolher sua opção! ')

    if opcao == 1:
        try:
            pedir_primeiro = int(input('Digite o primeiro número: '))
            pedir_segundo = int(input('Digite o segundo número: '))
        except:
            print('Use apenas números para escolher sua opção!!! ')
        resultado = somar(pedir_primeiro,pedir_segundo)
        if resultado is not None:
            print(resultado)
    elif opcao == 2:
        try:
            pedir_primeiro = int(input('Digite o primeiro número: '))
            pedir_segundo = int(input('Digite o segundo número: '))
        except:
            print('Use apenas números para escolher sua opção!!! ')
        resultado = subtrair(pedir_primeiro,pedir_segundo)
        if resultado is not None:
            print(resultado)
    elif opcao == 3:
        try:
            pedir_primeiro = int(input('Digite o primeiro número: '))
            pedir_segundo = int(input('Digite o segundo número: '))
        except:
            print('Use apenas números para escolher sua opção!!! ')
        resultado = mult(pedir_primeiro,pedir_segundo)
        if resultado is not None:
            print(resultado)
    elif opcao == 4:
        try:
            pedir_primeiro = int(input('Digite o primeiro número: '))
            pedir_segundo = int(input('Digite o segundo número: '))
        except:
            print('Use apenas números para escolher sua opção!!! ')
        resultado = dividir(pedir_primeiro,pedir_segundo)
        if resultado is not None:
            print(resultado)
    elif opcao == 5:
        print('Saindo do programa...')
        break
