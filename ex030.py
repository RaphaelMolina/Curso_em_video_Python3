e = str(' Exercício 30 ')
print('{:=^30}\n'.format(e))
print('Verificador de Ímpar e Par.\n')
numero = int(input('Informe um número para ser verificado: '))
resultado = numero %2
if numero % 2 == 0:
    print('\nO número {} é Par!'.format(numero))
else:
    print('\nO número {} é Ímpar!'.format(numero))
if resultado == 0:
    print('\nO número {} é Par!'.format(numero))
else:
    print('\nO número {} é ímpar!'.format(numero))
