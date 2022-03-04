'''
galera = [['Naira', 22], ['Meire', 54], ['Marta', 45], ['Ágata', 20]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])'''

# Exemplo:
'''
galera = [['Naira', 22], ['Meire', 54], ['Marta', 45], ['Ágata', 20]]
for p in galera:
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

# Exemplo:
'''
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)'''

# Exemplo:
galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')