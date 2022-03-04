# Função
# Exemplo:
'''
ef somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

# Programa Principal
somar(3, 2, 5)
somar(2, 2)
somar(4)'''

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


# Programa Principal
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')