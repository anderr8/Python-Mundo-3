# Reescresva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido.Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

# Função
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\33[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar nunhum número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31musuário preferiu não digitar nenhum número.\033[m')
            return 0
        else:
            return n

# Programa Principal
n1 = leiaInt('Digite um valor Inteiro: ')
n2 = leiaFloat('digite um valor Real: ')
print(f'O valor interio digiitado foi {n1} e o valor real foi {n2}.')
