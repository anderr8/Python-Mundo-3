# programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# mostre uma mesagem com  tamanho adaptável.
# Ex:
# escreva('Olá, Mundo!')Saída:
# ~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~


def escreva(msg):
    tam = len(msg) + 2
    print('~'*tam)
    print(f' {msg}')
    print('~'*tam)


# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso em Python no Youtube')
escreva('CeV')