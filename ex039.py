from datetime import datetime

e = str('Exercício 39')
#Neste tipo de format o f fica no começo antes das aspas simples, e as informações são colocadas dentro das chaves.
print(f'\n\033[31m{"":=^15}\033[m \033[35m{e}\033[m \033[34m{"":=^15}\033[m')

print('\n\033[4;32mVerificação de idade para o serviço militar!!\033[m')

nascimento = int(input('\nInforme o ano de seu nascimento para a verificação: '))

data = datetime.now()
idade = int(data.year - nascimento)

if idade < 18:
    print('\nVocê tem \033[34m{}\033[m anos, para se alistar é necessário ter no mínimo \033[1;31m18\033[m anos!'
          .format(idade))
    print('Você ainda não pode se alistar, fata(m) \033[35m{}\033[m ano(s) para que possa se alistar!'
          .format(18 - idade))
elif idade > 18:
    print('\nVocê tem \033[34m{}\033[m anos, para se alistar é necessário ter no mínimo \033[1;31m18\033[m anos!'
          .format(idade))
    print('Já passou do tempo de se alistar, passaram-se \033[35m{}\033[m ano(s) do período para se alistar!'
          .format(idade - 18))
else:
    print('\nVocê tem \033[34m{}\033[m anos, para se alistar é necessário ter no mínimo \033[1;31m18\033[m anos!'
          .format(idade))
    print('Esta na hora de se alistar, Vá até um posto do serviço militar para se apresentar!')
