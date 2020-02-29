from Titulo import Titulo

a = Titulo(16, 'Estruturas Compostas!!!')
a.Aula()
a = 2, 5, 4
b = 5, 8, 1, 2
# Concatena as Tuplas:
c = a + b
d = b + a

pessoa = ('Raphael', 30, 'M', 90.00)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')  # Tupla
# Tuplas são imutáveis

lanche1 = []  # Lista
lanche2 = {}  # Dicionário

# Fatiamento da Tupla:
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])

# Tamanho da Tupla:
print(len(lanche))

# Apresentando os Objetos da Tupla:
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!')

for contador in range(0, len(lanche)):
    print(contador)

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]}. Na posição {contador}.')
print('Comi pra caramba!')

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}. Na posição {posicao}!')
print('Comi pra caramba!')

print(sorted(lanche))  # Coloca a Tupla em ordem, como uma lista

print(a)
print(b)
print(c)
print(sorted(c))  # Coloca a Tupla em ordem, como uma lista
print(len(c))  # Tamanho da Tupla:
print(c.count(5))  # Verifica quantas vezes o item aparece
print(c.index(8))  # Mostra a posição da primeira ocorrência do Objeto
print(d)
print(d.index(5, 1))  # n1(Objeto da Tupla), n2(Início da busca), n3(Fim da busca)
print(pessoa)
del pessoa  # Deleta a Tupla
