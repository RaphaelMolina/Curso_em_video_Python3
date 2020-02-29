d = str(' Desafio 40 ')
print(f'\n{d:=^50}')

nota1 = float(input('\nPrimeira nota: '))
nota2 = float(input('Segunda nota: '))

média = float((nota1 + nota2) / 2)

print('\nTirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1, nota2, média))

if 7 > média >= 5:
    print('\nO aluno esta em recuperação!')
# Ou também pode ser feito desta forma.
# if média >= 5 and média < 7:
#     print('\nO aluno esta em recuperação!')
elif média < 5:
    print('\nO aluno esta reprovado!')
elif média >= 7:
    print('\nO aluno esta aprovado!')

