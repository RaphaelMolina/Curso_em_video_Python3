d = str(' Desafio 38 ')
print(f'\n{d:=^50}')

número1 = int(input('\nPrimeiro número: '))
número2 = int(input('Segundo número: '))

if número1 > número2:
    print('\nO Primeiro número é maior!!!')
elif número2 > número1:
    print('\nO Segundo número é maior!!!')
else:
    print('\nOs dois valores são iguais!!!')
