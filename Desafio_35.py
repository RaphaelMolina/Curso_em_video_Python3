d = str(' Desafio 35 ')
print('{:=^30}\n'.format(d))

print('Verificando se é possível formar um triângulo.\n')

reta1 = float(input('Informe o tamanho da primeira reta em cm: '))
reta2 = float(input('Informe o tamanho da segunda reta em cm: '))
reta3 = float(input('Informe o tamanho da terceira reta em cm: '))

if reta1 > (reta3 - reta2) and reta1 < (reta3 + reta2):
    if reta2 > (reta1 - reta3) and reta2 < (reta1 + reta3):
        if reta3 > (reta1 - reta2) and reta3 < (reta1 + reta2):
            print('\nAs retas informadas podem criar um triângulo!')
else:
    print('\nAs retas informadas não podem criar um triângulo!')
