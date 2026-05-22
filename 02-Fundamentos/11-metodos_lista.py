listaFilmes = ["Matrix", "Harry Potter", "Apocalipse",
               "Guerra dos Mundos", "xXx", "Devorador de planetas",
               "Interestrelar"]

# Tamanho de uma lista
print(len(listaFilmes))

# Recuperar um ítem da lista pelo nome
print(listaFilmes.index("xXx"))

# Adicionar um filme ao final da lista

print(
    f"Adicionando filme: O senhor dos anéis na lista: {listaFilmes.append("O senhor dos anéis")}\n posição: {len(listaFilmes)} \nlista {listaFilmes}")
print(len(listaFilmes))
