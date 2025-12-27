numero = int(input('Digite um número: '))

while numero != 0:
    if numero % 2 == 0:
        print('É par!')
    else:
        print('É ímpar!')

    numero = int(input('Digite outro número: '))

print('Fim do programa.')
