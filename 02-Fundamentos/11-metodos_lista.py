listaFilmes = ["Matrix", "Harry Potter", "Apocalipse",
               "Guerra dos Mundos", "xXx", "Devorador de planetas",
               "Interestrelar"]

# Tamanho de uma lista
print(len(listaFilmes))

# Recuperar um ítem da lista pelo nome
print(listaFilmes.index("xXx"))

# Adicionar um filme ao final da lista
listaFilmes.append("O senhor dos anéis")
print(len(listaFilmes))

# Ordenar a lista
listaFilmes.sort()
print(listaFilmes)

# Copiar os itens de uma lista para outra
copiaFilmes = listaFilmes.copy()  # Copiei para uma nova lista
print(copiaFilmes)
copiaFilmes.remove("xXx")  # remove um item da lista
print(copiaFilmes)

# Remove todos os itens de uma lista
listaFilmes.clear()  # Apaga toda a lista
print(listaFilmes)
