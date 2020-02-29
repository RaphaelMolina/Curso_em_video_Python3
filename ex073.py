from Titulo import Titulo

e = Titulo(73, 'Tabela do campeonato Brasileiro de Futebol!!!')
e.Exercicio()

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

ordem = sorted(times)

print('*=' * 30)
print('Lista de Times do Brasileirão:\n')
for time in times:
    if time == times[4] or time == times[9] or time == times[14]:
        print(f'{time},')
    elif time == times[19]:
        print(f'{time}.')
    else:
        print(time, end=', ')

print('*=' * 30)
print('Os 5 primeiros colocados são:\n')
for time in range(0, 5):
    if time == 4:
        print(f'{times[time]}.')
    else:
        print(times[time], end=', ')

print('*=' * 30)
print('Os últimos 4 colocados são: \n')
for time in range(16, 20):
    if time == 19:
        print(f'{times[time]}.')
    else:
        print(times[time], end=', ')

print('*=' * 30)
print('Lista de Times do Brasileirão em ordem alfabética:\n')
for time in ordem:
    if time == ordem[4] or time == ordem[9] or time == ordem[14]:
        print(f'{time},')
    elif time == ordem[19]:
        print(f'{time}.')
    else:
        print(time, end=', ')

print('*=' * 30)

print(f'O Chapecoense está na {times.index("Chapecoense") + 1}º posição.')
