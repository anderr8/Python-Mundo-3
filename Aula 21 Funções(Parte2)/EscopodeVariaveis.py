# Função
# O que está entre as linha é um escopo global
#----------------------------------------------
def teste():
    x = 8 # x é chamada de variável local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa principal

n = 2 # n o é chamada de variável global
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}') # x -> esse parâmetro dá erro porque não está daclarado no escopo Global,
                                            # mas sim está no escopo local

#----------------------------------------------


# O que está dendro dos sinais de igual são um escopo LOCAL
# O que está dentro dos pontilhados são um escopo GLOBAL

#------------------------------------
# Escopo Local
#==================================
def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')

#==================================
# Escopo Global
n1 = 2
função()
print(f'N1 global vale {n1}')
#------------------------------------