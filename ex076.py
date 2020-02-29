from Titulo import Titulo

e = Titulo(76, 'Produtos e Preços na Tupla!!!')
e.Exercicio()

tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25,
         'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32,
         'Canetas', 22.30, 'Livro', 34.90, 'Sulfite', 8.75)

print('-' * 45)
print(f'{"Listagem de Preços": ^45}')
print('-' * 45)
tamanho = len(tupla)

for contador in range(0, tamanho, 2):
    print(f'{tupla[contador]:.<35}R$ {tupla[contador + 1]: >6.2f}')
print('-' * 45)
