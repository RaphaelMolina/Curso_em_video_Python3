limpar = str('\033[m')
texto = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'verde_azul': '\033[36m'}
nome = input('{}Qual é o seu nome?{} '.format(texto['verde_azul'], limpar))
print('É um grande prazer te conhecer', nome)
