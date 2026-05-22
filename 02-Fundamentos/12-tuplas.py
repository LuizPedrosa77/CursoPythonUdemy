"""
    A principal diferença entre listas e tuplas em Python é que as listas são mutáveis 
    (podem ser alteradas após criadas), enquanto as tuplas são imutáveis 
    (não podem ter seus elementos modificados, adicionados ou removidos).
    """

tuplaFilmes = ("Matrix", "Harry Potter", "Apocalipse",
               "Guerra dos Mundos", "xXx", "Devorador de planetas",
               "Interestrelar")

print(type(tuplaFilmes))

# Buscar os 2 primeiros itens da tupla
print(tuplaFilmes[:2])

# Buscar o ultimo item da tupla
print(tuplaFilmes[-1])

# Buscar filmes de uma posição em diante
print(tuplaFilmes[2:5])

# Recuperar um item da tupla pelo nome
print(tuplaFilmes.index("Harry Potter"))
