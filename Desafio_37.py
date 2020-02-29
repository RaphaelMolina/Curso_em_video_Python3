d = str(' Desafio 37 ')
print(f'\n{d:=^50}')

número = int(input('\nDigite um número inteiro: '))

print('''\nEscolha uma das bases para a conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')

opção = int(input('\nDigite a sua opção: '))

if opção == 1:
    print('\n{} convertido para Binário é igual a {}.'.format(número, bin(número)[2:]))
elif opção == 2:
    print('\n{} convertido para Octal é igual a {}.'.format(número, oct(número)[2:]))
elif opção == 3:
    print('\n{} convertido para Hexadecimal é igual a {}.'.format(número, hex(número)[2:]))
else:
    print('''\nOpção inválida.
Tente novamente!''')
