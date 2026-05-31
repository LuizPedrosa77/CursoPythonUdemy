# Listando valores de 0 a 10
print("\n---- Listando valores de 0 a 9 ----")
listaNumero = [i for i in range(10) if i < 4]
print(listaNumero)

# Listando valores de 1 a 7
print("\n---- Listando valores de 1 a 7 ----")
listaNumero = [i for i in range(1, 7)]
print(listaNumero)

# Listando valores e 1 a 15 e maiores que 5
print("\n---- Listando valores e 1 a 15 e maiores que 5 ----")
listaNumero = [i for i in range(15) if i > 5]
print(listaNumero)

# Lista de filmes
filmeLista = ["Interestrelar", "Harry Potter",
              "xXx", "Jesus", "Paixão de Cristo"]

# Filmes que possuem a letra 'e' no titulo
print("\n---- Filmes que possuem a letra 'e' no titulo ----")
filmeExemplo = [filme for filme in filmeLista if 'a' in filme.lower()]
print(filmeExemplo)

# Filmes que eu assisti
print("\n---- Filmes que eu assisti -----")
filmeAssistidos = [filme for filme in filmeLista if filme != "xXx"]
print(filmeAssistidos)

# Encontrar um filme pelo nome
print("\n---- Encontrar um filme pelo nome ----")
while True:
    procurarNome = input(
        "\nDigite o nome do filme para procurar na lista (ou digite sair para encerrar):\n ")
    if procurarNome.lower() == "sair":
        print("\nPrograma encerrado!\n")
        break

    encontrarFilme = [
        filme for filme in filmeLista if procurarNome.lower() in filme.lower()]
    if encontrarFilme:
        print(f"\nATENÇÃO!!\nFilme encontrado com o nome {procurarNome}\n")
        for encontrarFilme in encontrarFilme:
            print(encontrarFilme)
    else:
        print(
            f"\nQue pena!\n Nenhum filme foi encontrado com o nome {procurarNome}. Tente novamente!\n")
