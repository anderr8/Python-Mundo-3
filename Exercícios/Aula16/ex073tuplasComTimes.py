# criar uma tupla preenchida com os 20 primeiros times do Brasileirão, na ordem de classificação.
# Mostar:
# a) Os 5 primeiros.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabetica.
# d) em que posição está o time da Chapecoense, não está classificado por foi rebaixado.

times = ('Internacional', 'Atletico-MG', 'Flamengo', 'São Paulo', 'Fluminense', 'Palmeiras', 'Santos',
         'Grêmio', 'Sport Recife', 'Corinthians', 'Fortaleza', 'Ceará SC', 'Atlético-GO', 'Bahia',
         'Coritiba', 'Bragantino-SP', 'Botafogo', 'Vasco da Gama', 'Atlético-PR', 'Goiás')
'''
Exemplo:
print('-=' * 30)
print(f'Lista do Brasileirão: {times}')
print('=-=' * 30)'''


print('=-='*15)
for t in times:
    print(t)
print('=-='*15)
print(f'Os 5 primeiros são Times: {times[0:5]}')
print('=-='*15)
print(f'Os 4 últimos são Times: {times[-4:]}')
print('=-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-='*15)
print(f'O são paulo está na {times.index("São Paulo")+1}ª posição.')