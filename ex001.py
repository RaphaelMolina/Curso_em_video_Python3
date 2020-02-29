limpar = str('\033[m')

estilo = {'padrao': '\033[0m',
          'negrito': '\033[1m',
          'sublinhado': '\033[4m',
          'negativo': '\033[7m'}

texto = {'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'zul': '\033[34m',
         'roxo': '\033[35m',
         'verde_azul': '\033[36m',
         'cinza': '\033[37m'}

fundo = {'branco': '\033[40m',
         'vermelho': '\033[41m',
         'verde': '\033[42m',
         'amarelo': '\033[43m',
         'azul': '\033[44m',
         'roxo': '\033[45m',
         'verde_azul': '\033[46m',
         'cinza': '\033[47m'}

print('{}Olá{}{},{} {}Mundo!{}'.format(texto['vermelho'], limpar, texto['verde'], limpar, texto['roxo'], limpar))
