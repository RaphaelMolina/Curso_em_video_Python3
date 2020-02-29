a = str(' Aula 11 ')
b = int(3)
c = int(5)
nome = str('Raphael')

style = {'default':'\033[0m',
         'negrito':'\033[1m',
         'sublinhado':'\033[4m',
         'negativo':'\033[7m'}

limpar = str('\033[m')

text = {'branco':'\033[30m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'amarel0':'\033[33m',
        'azul':'\033[34m',
        'roxo':'\033[35m',
        'verde_claro':'\033[36m',
        'cinza':'\033[37m'}

back = {'branco':'\033[40m',
        'vermelho':'\033[41m',
        'verde':'\033[42m',
        'amerelo':'\033[43m',
        'azul':'\033[44m',
        'roxo':'\033[45m',
        'verde_claro':'\033[46m',
        'cinza':'\033[47m'}

print('\033[4;35m{:=^30}\033[m\n'.format(a))
print('\033[7;30mOlá, Mundo!\033[m')
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(b, c))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('Olá! Muito prazer em te conhecer, {}{}{}{}{}!!!'.format(style['sublinhado'], text['vermelho'], back['verde_claro'], nome, limpar))
