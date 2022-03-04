# Algoritmo para gerar cinco números aleátorios e colocar em uma tupla. depois disso, mostrar a listagem
# de números gerados e também indique o menor e o maior valor que eatão na tupla.

from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\n) maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')