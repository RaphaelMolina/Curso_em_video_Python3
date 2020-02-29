from unidecode import unidecode
from Titulo import Titulo

e = Titulo(65, 'Média, Maior e Menor!!!')
e.Exercicio()

contador = media = maior = menor = n = int()
resposta = str('S')
while resposta[0] != 'N':
    contador += 1
    n = int(input('Informe um número: '))
    resposta = unidecode(str(input('Quer digitar outro número [S / N]? '))).upper().replace(' ', '')
    media += n
    if contador == 1:
        maior = menor = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n

print(f'\nA média de todos os números digitados é de {media//contador}.')
print(f'O Maior número digitado foi o {maior}.')
print(f'E o Menor número digitado foi o {menor}.')
