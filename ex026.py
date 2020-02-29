e = str(' Exercício 26 ')
print('{:=^30}\n'.format(e))

frase = str(input('Digite uma frase: ')).strip().lower()
print('\nA letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('a') + 1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('a') + 1))
