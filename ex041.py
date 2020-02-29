from datetime import datetime
e = str('Exercício 41')
#Neste tipo de format o f fica no começo antes das aspas simples, e as informações são colocadas dentro das chaves.
print(f'\n\033[31m{"":=^15}\033[m \033[35m{e}\033[m \033[34m{"":=^15}\033[m')

print('\n\033[4;32mVerificação de categoria para natação!!!\033[m')

nascimento = int(input('\nInforme seu ano de nascimento para a verificação da categoria: '))
data = datetime.now()
idade = int(data.year - nascimento)

print('\nCategorias:')
print('Até 9 anos categoria \033[31mMirin\033[m.')
print('De 10 à 14 anos categoria \033[32mInfantil\033[m.')
print('De 15 à 19 anos categoria \033[33mJunior\033[m.')
print('Com 20 anos categoria \033[34mSênior\033[m.')
print('De 21 anos em diante categoria \033[35mMaster\033[m.')

if (idade >= 0) and (idade <= 9):
    print(f'\nVocê tem {idade} anos. Sua categoria é a \033[31mMirin\033[m!')
elif (idade > 9) and (idade <= 14):
    print(f'\nVocê tem {idade} anos. Sua categoria é a \033[32mInfantil\033[m!')
elif (idade > 14) and (idade <= 19):
    print(f'\nVocê tem {idade} anos. Sua categoria é a \033[33mJunior\033[m!')
elif idade == 20:
    print(f'\nVocê tem {idade} anos. Sua categoria é a \033[34mSênior\033[m!')
elif idade > 20:
    print(f'\nVocê tem {idade} anos. Sua categoria é a \033[35mMaster\033[m!')
