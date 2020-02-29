from Titulo import Titulo

d = Titulo(53, 'Detector de Palíndromo!!!')
d.Desafio()

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso1 = junto[::-1]
for contador in range(len(junto) - 1, -1, -1):
    inverso += junto[contador]
print('\nO inverso de {} é {}.'.format(junto, inverso))
print('\nO inverso de {} é {}.'.format(junto, inverso1))
if inverso == junto:
    print('\nTemos um palíndromo!')
else:
    print('\nA frase digitada não é um palíndromo!')
if inverso1 == junto:
    print('\nTemos um palíndromo!')
else:
    print('\nA frase digitada não é um palíndromo!')




