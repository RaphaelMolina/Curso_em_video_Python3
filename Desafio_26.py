d = str(' Desafio 26 ')
print('{:=^30}\n'.format(d))

frase = str(input('Digite uma frase para análise: '))
print('\nA frase digitada tem {} A.'.format(frase.lower().count('a')))
print('A letra A aparece na posição {} primeiro.'.format(frase.lower().find('a')))
print('A letra A aparece na posição {} por último.'.format(frase.lower().rfind('a')))
