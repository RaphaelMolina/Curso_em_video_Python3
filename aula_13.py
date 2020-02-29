a = str(' Aula 13 ')
print(f'\033[34m{"=-*" * 10}\033[m\033[35m{a}\033[m\033[34m{"=-*" * 10}\033[m\n')
#Estrutura de repetição com variável de controle!
for contador in range(0, 6):
    print(contador)
print('Fim!\n')

for contador in range(0, 6, 1):
    print(contador)
print('Fim!\n')

for contador in range(5, -1, -1):
    print(contador)
print('Fim!\n')

for contador in range(0, 11, 2):
    print(contador)
print('Fim!\n')

n = int(input('Digite um número para finalizar a contagem: '))
for c in range(0, n + 1):
    print(c)
print('Fim!\n')

print('         \033[4mContagem!!!\033[m      ')
i = int(input('Informe o início da contagem: '))
f = int(input('Informe o fim da contagem: '))
p = int(input('Informe o pulo da contagem: '))
for c in range(i, f + 1, p):
    print(c)
print('Fim!\n')

s = int()
s1 = int()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    s += n
    s1 = s1 + n
print('\nA soma de todos os números digitados é \033[31m{}\033[m!!!'.format(s))
print('A soma de todos os números digitados é \033[36m{}\033[m!!!\n'.format(s1))
print('Fim!\n')

