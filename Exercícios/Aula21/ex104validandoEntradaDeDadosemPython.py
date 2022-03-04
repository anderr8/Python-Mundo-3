# Crie um programa que tenha a função leia(), que vai funcionar de form a semelhante á função input() do Python, só
# que fazendo  validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')
# função
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0:31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')