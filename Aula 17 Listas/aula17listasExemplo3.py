a = [2, 3, 4, 7]
b = a
b = a[:] # => comando para receber uma cópia da a em b
b[2] = 8 # trocando o número 2 por 8

print(a)
print(b)
print(f'Lista A: {a}')
print(f'Lista B: {b}')