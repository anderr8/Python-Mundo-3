def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

# Programa Principal


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# Desempacotando Valores

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valors {valores} temos {s}')


# Programa Principal


soma(5, 2)
soma(2, 9, 4)