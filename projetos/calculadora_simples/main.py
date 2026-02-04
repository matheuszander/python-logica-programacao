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

def pedir_dois_numeros():
    while True:
        try:
            n1 = int(input('Escolha o primeiro número: '))
            n2 = int(input('Escolha o segundo número: '))
            return n1,n2
        except:
            print('Use apenas números para escolher!')

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
        a,b = pedir_dois_numeros()
        resultado = somar(a,b)
        if resultado is not None:
            print(resultado)
    elif opcao == 2:
        a,b = pedir_dois_numeros()
        resultado = subtrair(a,b)
        if resultado is not None:
            print(resultado)
    elif opcao == 3:
        a,b = pedir_dois_numeros()
        resultado = mult(a,b)
        if resultado is not None:
            print(resultado)
    elif opcao == 4:
        a,b = pedir_dois_numeros()
        resultado = dividir(a,b)
        if resultado is not None:
            print(resultado)
    elif opcao == 5:
        print('Saindo do programa...')
        break
