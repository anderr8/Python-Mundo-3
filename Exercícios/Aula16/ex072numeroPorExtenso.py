# Algoritmo que tenha uma tupla de zero até vinte. O programa deverá ler um número pelo teclado e
# mostrá-lo por extenso.


cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 até 20: '))
    if 0 <= núm >= 20:
        print('O número digitado não está entre 0 e 20. ', end='')
    else:
        print(f'Você digitou o número {cont[núm]}.')
    resp = ' '
    while resp not in 'SN':
       resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
       break
print('Programa Finalizado.')
