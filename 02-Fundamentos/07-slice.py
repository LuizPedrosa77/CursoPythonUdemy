nomeFilme = "Top Gun"
# string[inicio:fim] - indice começa na posição ZERO e termina na posição -1

# 1 - Buscar toda string a partir a primeira posição
print(nomeFilme[0:])

# 2 - Buscar toda string até a ultima posição
print(nomeFilme[:-1])
print(nomeFilme[:6])

# 3 - Buscar string da terceira posição
print(nomeFilme[2:])

'''
string[inicio:fim:passo]
indice começa na posição 0 e termina na posição -1
passo - determina o incremento e por padrão esse número é -1
'''

# 4 - Busca toda a string de 2 em 2 caractere
print(nomeFilme[::2])

# 5 - Busca toda string no indice ímpar
print(nomeFilme[1::2])

# 6 - Inverte a string de trás para frente
print(nomeFilme[::-1])
