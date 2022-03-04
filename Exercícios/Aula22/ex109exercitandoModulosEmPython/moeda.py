def aumentar(preço=0, taxa=0, formato=False):
    '''

    :param preço:
    :param taxa:
    :param formato:
    :return:
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res) # exemplo: é possivel usar o not não é necessário usar o False


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')