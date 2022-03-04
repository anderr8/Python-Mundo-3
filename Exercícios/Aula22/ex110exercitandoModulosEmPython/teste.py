#  Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela
#  algumas informações geradas pelas funções que já temos no módulo criado até aqui.
# Programa Principal

from ex110exercitandoModulosEmPython import moeda
#import moeda exemplo

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)




'''p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')'''
