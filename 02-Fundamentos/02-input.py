# Utilizando input

'''
Quando se usa INPUT ele transforma em string e por isso há necessidade de conversão
'''

nome = input("Digite o nome do filme: \n")
anoLancamento = int(input("Digite o ano de lancamento: \n"))  # conversão
notaFilme = float(input("Digite a nota do filme: \n"))  # conversão

print(type(nome))
print(type(anoLancamento))
print(type(notaFilme))
