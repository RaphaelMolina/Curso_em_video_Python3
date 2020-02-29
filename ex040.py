e = str('Exercício 40')
#Neste tipo de format o f fica no começo antes das aspas simples, e as informações são colocadas dentro das chaves.
print(f'\n\033[31m{"":=^15}\033[m \033[35m{e}\033[m \033[34m{"":=^15}\033[m')

print('\n\033[4;32mCalculando a média de um aluno!!!\033[m')

nota1 = float(input('\nInforme a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))

media = float((nota1 + nota2)/2)

print('\nRegras do sistema:')
print('Médias de 0 até 4.99: \033[31mReprovado\033[m.')
print('Médias de 5 até 6.99: \033[36mRecuperação\033[m.')
print('Médias de 7 em diante: \033[32mAprovado\033[m.')

if media < 5.0:
    print('\nSua média foi de \033[34m{:.2f}\033[m.'.format(media))
    print('Você foi \033[31mReprovado!!!\033[m')
elif (media >= 5.0) and (media <= 6.99):
    print('\nSua média foi de \033[34m{:.2f}\033[m.'.format(media))
    print('Você ficou de \033[36mRecuperação!!!\033[m')
else:
    print('\nSua média foi de \033[34m{:.2f}\033[m.'.format(media))
    print('Você foi \033[32mAprovado!!!\033[m')


