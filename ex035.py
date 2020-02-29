e = str(' Exercício 35 ')
print('{:=^30}\n'.format(e))
print('*=*' * 23)
print('Verificando se as retas informadas podem formar um triângulo.')
print('*=*' * 23)
reta1 = float(input('\nInforme a primeira reta em cm: '))
reta2 = float(input('Informe a segunda reta em cm: '))
reta3 = float(input('Informe a terceira reta em cm: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas informadas podem formar um triâgulo!')
else:
    print('As retas informadas não podem formar um triângulo!')
