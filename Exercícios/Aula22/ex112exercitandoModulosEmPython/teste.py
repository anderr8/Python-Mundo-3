#  Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
#  leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para
#  aceitar apenas valores que seja monetários.
# Programa Principal

from ex112exercitandoModulosEmPython.utilidadescev import moeda
from ex112exercitandoModulosEmPython.utilidadescev import dado

#import moeda exemplo

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)




'''p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')'''
