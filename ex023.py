e = str(' Exercício 23 ')
print('{:=^30}\n'.format(e))

numero = int(input('Digite um número entre 0 e 9999: '))
converte = str(numero)# Convertendo o int em str
print('\nAnalisando o número {}, podemos dizer que temos:'.format(numero))
# Deste modo só funciona para número com quatro dígitos
print('Unidade: {}'.format(converte[3]))
print('Dezena:  {}'.format(converte[2]))
print('Centena: {}'.format(converte[1]))
print('Milhar:  {}'.format(converte[0]))
# Ou
# Separando os números
unidade = numero % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('\nUnidade: {}'.format(unidade))
print('Dezena:  {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar:  {}'.format(milhar))

