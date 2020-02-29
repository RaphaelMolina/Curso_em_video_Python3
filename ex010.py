limpar = str('\033[m')

texto = {'vermelho': '\033[31m',
         'roxo': '\033[35m',
         'verde2': '\033[36m'}

e = str('{} Exercício 10 {}'.format(texto['vermelho'], texto['verde2']))
print('{}{:=^30}{}\n'.format(texto['verde2'], e, limpar))

real = float(input('{}Informe o valor que você tem: R${}'.format(texto['roxo'], limpar)))
dolar = float(real / 3.27)

print('Você tem {}R${:.2f}{}, e com esse valor você pode comprar {}US${:.2f}{}.'.format(texto['vermelho'], real, limpar,
                                                                                        texto['verde2'], dolar, limpar))
