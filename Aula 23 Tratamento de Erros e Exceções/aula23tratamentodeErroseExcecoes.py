# Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar
# a estrutura try except no Python de uma forma simples.


# Tratamento de Erro:
try: # tente fazer isso
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#exemplo:
#except: # se falhou
#except Exception as erro: # (Exception)-> Classe principal
except(ValueError, TypeError):
    #print('Infelizmente tivemos um problema :(') -> exemplo
    #print(f'Problema encontrado foi {erro.__class__}')
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: # se deu certo
    print(f'O resultado é {r:.1f}')
finally: # vai acontecer se der certo ou não
    print('Volte sempre! Muito obrigado!')
