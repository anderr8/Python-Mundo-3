# Algoritmo que tenha uma tupla com várias palavras(não usar acentos). Depoisdisso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'práticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p. upper()} temos.', end='')
    for letra in p:
       if letra.lower() in 'aáãâeéêioóôuú':
           print(letra, end=' ')