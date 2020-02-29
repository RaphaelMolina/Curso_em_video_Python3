d = str(' Desafio 30 ')
print('{:=^30}\n'.format(d))
print('Verificador de Ímpar e Par.\n')
numero = int(input('Informe um número inteiro: '))
verificador = numero % 2
if numero == 0:
    print('Número Neuto!')
else:
    if verificador == 0:
        print('Par!')
    else:
        print('Ímpar!')