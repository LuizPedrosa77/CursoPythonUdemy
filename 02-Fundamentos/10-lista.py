filmeMatrix = ["Matrix", 1999, 8.7, True]
print(filmeMatrix)

listaFilmes = ["Matrix", "Harry Potter", "Apocalipse",
               "Guerra dos Mundos", "xXx", "Devorador de planetas",
               "Interestrelar"]

print(f"1-Começa a partir do 2º da lista {listaFilmes[2:]}\n"
      f"2-Mostra apenas os 2 primeiros da lista {listaFilmes[:2]}\n"
      f"3-Ultimo filme da lista {listaFilmes[-1]}\n"
      f"4-Busca filmes a partir de uma posição em diante {listaFilmes[1:6]}\n"
      )

print(listaFilmes[2:])  # Começa a partir o 2º a lista
print(listaFilmes[:2])  # Só mostra apenas os 2 primeiros da lista
