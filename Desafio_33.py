d = str(' Desafio 33 ')
print('{:=^30}\n'.format(d))
print('Verificando o maior e menor número\n')
numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
    print('\nO maior número informado é o número: {}'.format(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print('\nO maior número informado é o número: {}'.format(numero2))
elif numero3 > numero1 and numero3 > numero2:
    print('\nO maior número informado é o número: {}'.format(numero3))
else:
    print('\nNão foi possível localizar o maior número, por favor informe números diferentes entre si!')

if numero1 < numero2 and numero1 < numero3:
    print('O menor número informado é o número: {}'.format(numero1))
elif numero2 < numero1 and numero2 < numero3:
    print('O menor número informado é o número: {]'.format(numero2))
elif numero3 < numero1 and numero3 < numero2:
    print('O menor número informado é o número: {}'.format(numero3))
else:
    print('Não foi possível localizar o menor número, por favor informe números diferentes entre si!')
