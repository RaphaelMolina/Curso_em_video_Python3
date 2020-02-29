from time import sleep
from emoji import emojize

e = str('Exercício 46')
print(f' \n \33[31m {"=" * 15} \33[m \33[35m {e} \33[m \33[34m {"=" * 15} \33[m')

print(f'\n{" " * 13}\33[4;32mContagem Regressiva!!!\33[m')

for contador in range(10, -1, -1):
    sleep(1)
    print(contador)
    # :tada: = Cone com confeti \U0001F942 = taças  \U0001F389 = Cone com confeti \U0001F38A = Confeti superior
sleep(1)

print(emojize('\n:tada: \U0001F942 \U0001F38A Feliz Ano Novo!!! \U0001F389 \U0001F942 \U0001F38A',
              use_aliases=True))
