e = str('Exercício 47')
print(f'\n\33[31m{"=" * 15} \33[m\33[35m{e}\33[m\33[34m {"=" * 15}\33[m')

print(f"\n{' ' * 5}\33[4;32mNúmeros Pares entre o 01 e o 50!!!\33[m")

for contador in range(1, 51):

    if contador % 2 == 0:
        print(contador)
print('Fim!')

