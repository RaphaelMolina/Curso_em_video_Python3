print('============= Exercício 03 =============')
texto = {'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'verde2':'\033[36m'}
limpar = str('\033[m')
numero1 = int(input('Digite um valor para a adição: '))
numero2 = int(input('Digite mais um valor para realizar a operação: '))
resultado = numero1+numero2
print('A soma entre {}{}{} e {}{}{} é igual a: {}{}{}'. format(texto['vermelho'], numero1, limpar, texto['verde2'], numero2, limpar, texto['roxo'], resultado, limpar))
