#  Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar
#  os números como um valor monetário formatado.
# Programa Principal

from ex108exercitandoModulosEmPython import moeda
#import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.metade(p)}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')

