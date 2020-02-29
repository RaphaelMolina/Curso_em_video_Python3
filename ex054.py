from Titulo import Titulo

e = Titulo(54, 'Verificador da Maioridade!!!')
e.Exercicio()
# Neste caso iremos considerar 21 como sendo a maioridade.
a = int()
for contador in range(0, 7):
    i = int(input('Informe seu ano de nascimento: '))
    if i <= 1998:
        a += 1
if a > 1:
    print(f'\n\33[34m{a} pessoas já atingiram a Maioridade!!!\33[m')
    if a == 6:
        print(f'\n\33[35mUma pessoa ainda Não atingiu a Maioridade!!!\33[m')
    elif a == 7:
        print(f'\n\33[35mTodos atingiram a Maioridade!!!\33[m')
    else:
        print(f'\n\33[35m{7 - a} pessoas ainda Não atingiram a Maioridade!!!\33[m')
elif a == 1:
    print('\n\33[35mUma pessoa atingiu a Maioridade!!!\33[m')
    print('\n\33[34mSeis pessoas ainda Não atingiram a Maioridade!!!\33[m')
else:
    print('\n\33[31mNinguém atingiu a Maioridade!!!\33[m')