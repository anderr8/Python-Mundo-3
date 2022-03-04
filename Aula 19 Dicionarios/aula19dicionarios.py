# Para declarar é usado as CHAVES, e para referênciar é usado colchetes

'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')


print(pessoas.keys())
print(pessoas.items())'''

'''pessoas = {'nome': 'Anderson', 'sexo': 'M', 'idade': 41}
for k in pessoas.keys():
    print(k)'''

pessoas = {'nome': 'Anderson', 'sexo': 'M', 'idade': 41}
#del pessoas['sexo'] # del comando para deletar
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

