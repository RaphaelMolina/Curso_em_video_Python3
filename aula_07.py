# Ordem de Precedência:
# 1º Se resolve o que estiver entre ().
# 2º Se resolve ** Potência.
# 3º Se resolve * Multiplicação / Divisão // Divisão inteira e % Módulo.
# 4º Se resolve + Adição e - Subtração.

a = 5+2  # Adição.
b = 5-2  # Subtração.
c = 5*2  # Multiplicação.
d = 5/2  # Divisão.
e = 5**2 # Potência ou Exponenciação.
f = 5//2 # Divisão inteira = utiliza como resultado somente o número inteiro, sem o que estiver depois do ponto flutuante.
g = 5%2  # Módulo = resto da divisão.
#print(a, b, c, d, e, f, g)
h = 5+3*2
i = 3*5+4**2
j = 3*(5+4)**2
#print(h, i, j)
l = 9**(1/2) # Raiz quadrada.
m = 9**0.5   # Raiz quadrada.
n = 9**(1/3) # Raiz cúbica.
#print(l, m, n)
#nome = str(input('Qual é o seu nome? '))
# print('Prazer em te conhecer {}!'. format(nome))
# print('Prazer em te conhecer {:20}!'.format(nome))
# print('Prazer em te conhecer {:>20}!'.format(nome))
# print('Prazer em te conhecer {:<20}!'. format(nome))
# print('Prazer em te conhecer {:^20}!'. format(nome))
# print('Prazer em te conhecer {:=^20}!'. format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
adicao = n1+n2
multiplicacao = n1*n2
subtracao = n1-n2
divisao = n1/n2
divisao_inteira = n1//n2
exponenciacao = n1**n2
print('O resultado da soma entre os dois números é: {}'. format(n1+n2))
print('O resultado dos cálculos entre os dois números são: ')
print('Adição: {} \nMultiplicação: {} \nSubtração: {} '. format(adicao, multiplicacao, subtracao), end=' ')
print('Divisão: {:.2f} \nDivisão Inteira: {} \nExponenciação: {}'.format(divisao, divisao_inteira, exponenciacao))










