# Algoritmo que leia qutro valores pelo teclado e guarde-os em uma tupla. no final mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.

núm = (int(input('Dígite um número: ')),
       int(input('Dígite outro número: ')),
       int(input('Dígite mais um número: ')),
       int(input('Dígite uo último número: ')))
print(f'Você digitou os valores {núm}.')
print(f'O valor 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição.')
else:
   print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
       print(n, end=' ')