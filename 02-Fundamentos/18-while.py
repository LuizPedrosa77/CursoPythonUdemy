filmeLista = ["Interestrelar", "Harry Potter",
              "xXx", "Jesus", "Paixão de Cristo"]

# Interando valores de uma lista de filmes usando While
print("\n---- Interando valores de uma lista de filmes usando While ----")
index = 0
while index < len(filmeLista):
    print(filmeLista[index])
    index += 1

# Quando a condição for atendida o loop será encerrado
print("\n---- Quando a condição for atendida o loop será encerrado ----")
index = 0
while index < len(filmeLista):
    if filmeLista[index] == "Jesus":
        break
    print(filmeLista[index])
    index += 1

# Quando a condição for atendida ele vai para proxima interação
print("\n---- Quando a condição for atendida ele vai para proxima interação ----")
index = 0
while index < len(filmeLista):
    if filmeLista[index] == "xXx":
        index += 1
        continue
    print(filmeLista[index])
    index += 1

# Avaliação do filme
print("\n---- Avaliação do filme ----")
nomeFilme = input("Digite o nome do filme: \n")
avaliacaoFilme = int(input("Digite quantas avaliações deseja fazer: \n"))

count = 0
total = 0

while count < avaliacaoFilme:
    nota = float(input("Digite a nota o filme; \n"))
    total += nota
    count += 1

if avaliacaoFilme > 0:
    media = total / avaliacaoFilme
else:
    media = 0

print(f"A média da avalização do filme {nomeFilme} é {media:.2f}")
