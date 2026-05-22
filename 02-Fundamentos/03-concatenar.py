nome = input("Digite o nome do filme: \n")
anoLancamento = int(input("Digite o ano de lancamento: \n"))  # conversão
notaFilme = float(input("Digite a nota do filme: \n"))  # conversão
pularlinha = "\n"

print("Dados do filme")
print("===============")
print(pularlinha)
# Alternativa 1 -> individual
print("Alternativa 1 -> individual")
print("Nome do filme: ", nome)
print("Ano de lançamento: ", anoLancamento)
print("Nota do filme: ", notaFilme)
print(pularlinha)
# Alternativa 2 -> concatenado
print("Alternativa 2 -> concatenado")
print("Nome do filme: ", nome, "\nAno de lançamento: ",
      anoLancamento, "\nNota do filme: ", notaFilme)
print(pularlinha)
# Alternativa 3 -> f+string
print("Alternativa 3 -> f+string")
print(f"Nome do filme: {nome}\n"
      f"Ano de lançamento: {anoLancamento}\n"
      f"Nota do filme: {notaFilme}"
      )
