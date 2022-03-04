# Função
def contador(i, f, p):
# docstrings => começa depois do comando def
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal Curso em Video.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


# Programa Principal
contador(10, 100, 10)
help(contador) # => manual que sará exibido
