# Programa Principal
from ex115aCriandoUmMenu.lib.interface import *
from ex115aCriandoUmMenu.lib.ex115barquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not ex115barquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de listar o conteúdo de um arquivo.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de siar do sistema.
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        # Digitou uma opçaõ errada no menu.
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)
