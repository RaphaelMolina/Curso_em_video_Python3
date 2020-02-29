from Titulo import Titulo
from unidecode import unidecode

e = Titulo(53, 'Análise de Palíndromo!!!')

e.Exercicio()
# unidecode = Retira os acentos da frase.
# lower = Diminui todas as letras.
# replace = Retira todos os espaços.
# len = informa o número de caracteres.

#Palíndromos:
# Após a sopa
# A Sacada da casa
# A Torre da derrota
# O lobo ama o bolo
# Anotaram a data da maratona

f = unidecode(str(input('Digite uma frase para ser análisada: '))).lower().replace(' ', '')
t = len(f) - 1

if f[:: -1] == f[:: 1]:
    print('\n\33[34mEsta Frase é um Palíndromo!!!\33[m')
else:
    print('\n\33[31mEsta Frase NÃO é um Palíndromo!\33[m')
c = int()
for contador in range(0, t + 1):
    if f[contador] == f[t - contador]:
        c += 1
if c == t + 1:
    print('\n\33[34mEsta Frase é um Palíndromo!!!\33[m')
else:
    print('\n\33[31mEsta Frase NÃO é um Palíndromo!\33[m')



