# Tuplas são variáveis compostas e imutáves que permitem armazenar vários valores em uma mesma estrutura
# tuplas podem ser começadas por 3 tipos:
# () => Tuplas
# [] => Listas, pode ser para referênciar
# {} => Dicionários
# for pode ser para repetição, iteração
# sorted = organização, em ordem



lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') #-> ser tirados os parêtenses
# Formas de refêrencia
'''
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[0:])
print(lanche[:2])
print(lanche[-2:])
print(sorted(lanche)) -> comando para ordem'''

'''for comida in lanche:
for pos, comida in enumerate lanche: -> mostra a posição
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''

# Formas de fatiação
for cont in range(0, len(lanche)):
    print(cont)
    print(lanche[cont])
    print(f'Eu vou comer {lanche[cont]}')
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')