a = str('Aula 12')

Style = {'default':'\033[0m',
        'negrito':'\033[1m',
        'sublinhado':'\033[4m',
        'negativo':'\033[7m'}

limpar = str('\033[m')

text = {'branco':'\033[30m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'amarelo':'\033[33m',
        'azul':'\033[34m',
        'roxo':'\033[35m',
        'verde_claro':'\033[36m',
        'cinza':'\033[37m'}

back = {'branco':'\033[40m',
        'vermelho':'\033[41m',
        'verde':'\033[42m',
        'amarelo':'\033[43m',
        'azul':'\033[44m',
        'roxo':'\033[45m',
        'verde_claro':'\033[46m',
        'cinza':'\033[47m'}

print('\n{}{:=^30}{}\n'.format(text['roxo'], a, limpar))
nome = str(input('Qual é o seu nome? '))
if nome == 'Raphael':
        print('\n{}Que nome Bonito!{}'.format(text['verde_claro'], limpar))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
        print('\nSeu nome é bem popular no Brasil.')
elif nome in 'Beatrys Ana Cláudia Jéssica Juliana':
        print('\nBelo nome feminino!')
else:
        print('\nSeu nome é bem normal!')

print('Tenha um Bom dia, {}{}{}!'.format(text['azul'], nome, limpar))