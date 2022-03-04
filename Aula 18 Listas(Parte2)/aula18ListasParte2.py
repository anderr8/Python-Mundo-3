# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura
# , acesíveis por chaves individuais.

teste = list()
teste.append('Anderson')
teste.append(41)
#print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Clint'
teste[1] = 40
galera.append(teste[:]) # => [:] faz uma cópia
print(galera)