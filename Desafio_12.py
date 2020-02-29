d = str(' Desafio 12 ')
print('{:=^30}\n'.format(d))

p = float(input('Informe o valor do produto para calcular o desconto: R$ '))
d = float(p*.05)
np = float(p - d)
print('O valor informado tem 5% de desconto!\nO valor do produto com o desconto é de: R$ {}'.format(np))

