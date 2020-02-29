e = str('Exercício')
#Neste tipo de format o f fica no começo antes das aspas simples, e as informações são colocadas dentro das chaves.
print(f'\n\033[31m{"":=^15}\033[m \033[35m{e}\033[m \033[34m{"":=>15}\033[m')

print('\n\033[4;32mComparando os dois valores informados!!!\033[m')

numero1 = int(input('\nInforme um número inteiro como primeiro valor: '))
numero2 = int(input('Informe um número inteiro como segundo valor: '))

if numero1 > numero2:
    print('\nO primeiro valor informado foi \033[34m{}\033[m.'.format(numero1))
    print('O segundo valor informado foi \033[35m{}\033[m.'.format(numero2))
    print('Comparando os valores informados podemos ver que o \033[34mprimeiro\033[m valor é o \033[35mmaior\033[m!')
elif numero1 < numero2:
    print('\nO primeiro valor informado foi \033[34m{}\033[m.'.format(numero1))
    print('O segundo valor informado foi \033[35m{}\033[m.'.format(numero2))
    print('Comparando os valores informados podemos ver que o \033[34msegundo\033[m valor é o \033[35mmaior\033[m!')
else:
    print('\nO primeiro valor informado foi \033[34m{}\033[m.'.format(numero1))
    print('O segundo valor informado foi \033[35m{}\033[m.'.format(numero2))
    print('Comparando os valores informados podemos ver que o \033[34mprimeiro\033[m valor e o \033[35msegundo\033[m '
          'valor são \033[36miguais\033[m!')
