'''
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa
função.
- Os argumentos são passados como uma tupla
**kwargs - Além os valores, podemos passar também as respectivas chaves para cada argumentos.
- Os argumentos são passados como um dicionario
'''
linha = '='
# 1 Soma de numeros
print('Usando função args')


def soma(*num):
    soma_total = 0
    for n in num:
        soma_total += n
    print(f'Soma é: {soma_total}')


soma(7)
soma(1, 3)
soma(13, 28)
print(linha*50)
# 2 Apresentação de curso
print('Usando função kwargs')


def apresentacao(**data):
    for key, Values in data.items():
        print(f"{key} - {Values}")


print('---- Lista de cursos ----')
print('Curso 1')
apresentacao(nome='Python', categoria='Backend', nivel='Iniciante')
print('Curso 2')
apresentacao(nome='Visão computacional com Python',
             categoria='IA', nivel='Avançado')
print('Curso 3')
apresentacao(nome='Dashboard com Dash',
             categoria='Data Science', nivel='Intermediário')
