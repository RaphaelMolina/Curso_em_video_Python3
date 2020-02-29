from Titulo import Titulo
e = Titulo(72, 'Apresentação dos números por extenso!!!')
e.Exercicio()

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Informe um número de 0 a 20 para ver sua escrita por extenso: '))
while n not in range(0, 20):
    n = int(input('Tente novamente. Informe um número de 0 a 20: '))
print(f'Você digitou o número {numeros[n]}.')
