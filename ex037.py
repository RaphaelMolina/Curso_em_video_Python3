e = str('Exercício 37')
#Neste tipo de format o f fica no começo antes das aspas simples, e as informações são colocadas dentro das chaves.
print(f'\n \033[31m{"":=^15}\033[m \033[35m{e}\033[m \033[34m{"":=^15}\033[m')

print('\n \033[4;32mConversão de base númerica!!!\033[m')

numero = int(input('\nInforme um número decimal inteiro para a conversão de base: '))

print('\nEscolha a base de conversão:')
print('Digite 1 para a base \033[34mBinária\033[m.')
print('Digite 2 para a base \033[31mOctal\033[m.')
print('Ou Digite 3 para a base \033[36mHexadecimal\033[m.')

escolha = int(input('\nE então, qual base você irá escolher? '))

binario =     bin(numero)
octal =       oct(numero)
hexadecimal = hex(numero)

#Retirando o prefixo.
b = binario[2:]
o = octal[2:]
h = hexadecimal[2:]

if   escolha == 1:
    print('\nVocê escolheu a base Binária!')
    print('Você digitou \033[34m{}\033[m, sua representação Binária é: \033[35m{}\033[m.'.format(numero, b))
elif escolha == 2:
    print('\nVocê escolheu a base Octal!')
    print('Você digitou \033[34m{}\033[m, sua representação Octal é: \033[35m{}\033[m.'.format(numero, o))
else:
    print('\nVocê escolheu a base Hexadecimal!')
    print('Você digitou \033[34m{}\033[m, sua representação Hexadecimal é: \033[35m{}\033[m.'. format(numero, h.upper()))