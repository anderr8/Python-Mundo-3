#num = (2, 5, 9, 1) => tupla imútaveis
num = [2, 5, 9, 1] #=> lista mútaveis
num[2] = 3
num.append(7)
num.sort() # mostra a lista em ordem
num.sort(reverse=True) # mostra a lista de ordem reversa
num.insert(2, 0) # insere o número zero
if 4 in num: # comando para remover um número
    num.remove(4)
else:
    print('Não achei o número 4')
num.pop() # remove o último número
num.pop(2) # remove o número dois
print(num)
print(f'Essa lista tem {len(num)} elementos.')