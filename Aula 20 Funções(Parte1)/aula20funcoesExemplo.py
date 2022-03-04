# O que são funções e rotinas e como utilizar funções em Python. Funções são trechos de códigos que podem ser
# executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando (def) em Python e
# como utilizá-lo com parâmetros simples e mútiplos.

# Criando várias linhas(Rotinas)
# Função sem paramêtros:

def lin():
    print('-'*30)


# Programa Principal
lin()
print('   CURSO EM VIDEO   ')
lin()
lin()
print('   APRENDA PYTHON   ')
lin()
lin()
print('   GUSTAVO GUANABARA   ')
lin()

# Passando Parâmetro mostrando mensagem
# Função com Parâmetros:

def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

# Programa Principal
título('   CURSO EM VÍDEO   ')
título('   PYTHON É MUITO BOM!   ')
título('   OI   ')