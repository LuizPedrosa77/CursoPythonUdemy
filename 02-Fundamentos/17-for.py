filmeLista = ["Interestrelar", "Harry Potter",
              "xXx", "Jesus", "Paixão de Cristo"]

# Interando valores de uma lista usano FOR IN
print("\n---- Interando valores de uma lista ----")
for filme in filmeLista:
    print(filme)

# Quano a condição for atendida, o loop será encerrado!
print("\n---- Quando a condição for atendida, o loop será encerrado! ----")
for filme in filmeLista:
    if filme == "Jesus":
        break
    print(filme)

# Quando a condição for atendida, o loop vai para proxima interação
print("\n---- Quando a condição for atendida, o loop vai para proxima interação ----")
for filme in filmeLista:
    if filme == "Harry Potter":
        continue
    print(filme)

# Avaliação do filme
nomeFilme = input("Digite o nome do filme: \n")
avaliacaoFilme = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0
for i in range(avaliacaoFilme):
    nota = float(input("Digite a nota o filme; \n"))
    total += nota

if avaliacaoFilme > 0:
    media = total / avaliacaoFilme
else:
    media = 0

print(f"A média da avalização do filme {nomeFilme} é {media:.2f}")
