e = str(' Exercício 33 ')
print('{:=^30}\n'.format(e))
print('Verificando o maior e o menor número informado.\n')
numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print('\nO menor número informado foi o {}, e o maior número informado foi o {}.'.format(menor, maior))
menor1 = numero1
maior1 = numero1
if numero2 < numero1 and numero2 < numero3:
    menor1 = numero2
if numero3 < numero1 and numero3 < numero2:
    menor1 = numero3
if numero2 > numero1 and numero2 > numero3:
    maior1 = numero2
if numero3 > numero1 and numero3 > numero2:
    maior1 = numero3
print('\nO menor número informado foi o {}, e o maior número informado foi o {}.'.format(menor1, maior1))

