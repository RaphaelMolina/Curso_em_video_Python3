e = str('Exercício 48')
print(f'\n\33[31m{"=" * 15}\33[m \33[35m{e}\33[m \33[34m{"=" * 15}\33[m')

print('\n\33[4;32mSoma de todos os números ímprares, que são Múltiplos de três entre o intervalo de 01 a 500!!!\33[m\n')
soma = int()
for contador in range(1, 501):
    if contador % 3 == 0:
        soma += contador
print(soma)
print('Fim!')
