from Titulo import Titulo

d = Titulo(48, 'Soma de números ímpares múltiplos de três!!!')
d.Desafio()
soma = int() #Acumulador
cont = int() #Contador
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        soma += contador
        cont += 1
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
