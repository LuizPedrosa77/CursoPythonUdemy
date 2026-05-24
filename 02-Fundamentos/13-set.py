"""
    Listas são mutáveis, ordenadas e permitem duplicatas.
    Tuplas são imutáveis, ordenadas e permitem duplicatas.
    Sets (conjuntos) são mutáveis, não ordenados e não permitem duplicatas.
    """

setFilmes = {"Matrix", "Harry Potter", "Apocalipse",
             "Guerra dos Mundos", "xXx", "Devorador de planetas",
             "Interestrelar"}

print(type(setFilmes))

# True e 1 são considerados o mesmo valor dentro de Set
exemplo = {"primeiro", True, 1, 8.7}
print(exemplo)

# Adicionar item de outro Set
setFilmes.update(exemplo)
print(setFilmes)

# Remover um item do Set
setFilmes.remove("xXx")
print(setFilmes)
