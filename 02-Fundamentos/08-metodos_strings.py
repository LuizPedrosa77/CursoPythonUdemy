nomeFilme = "Top Gun"
descricaoFilme = """
    O filme Maverick, é um filme muito
    consagrado na industria, no mundo todo.
"""
linha = "="
print(f"---Trabalhano com manipulação de strings---\n"
      f"1 - Toda string em maiusculo: {nomeFilme.upper()}\n"
      f"2 - Toda string em minusculo: {nomeFilme.lower()}\n"
      f"3 - Apenas a primeira letra maiuculo: {nomeFilme.capitalize()}\n"
      f"4 - Todas as primeiras letras de cada palavra em maiusculo: {nomeFilme.title()}\n"
      f"5 - Retorna strings centralizadas com caracteres de preenchimento no inicio e final do texto: {nomeFilme.center(10, '-')}\n"
      f"6 - Retorna a posição ou indice de um determinado caracter: {nomeFilme.find("G")}\n"
      f"6.1 - Também serve para contar o caracter: {nomeFilme.find("o")}\n"
      f"7 - Altera (troca) elementos ou palavras por outro. Nome original: {nomeFilme}, nome alterado: {nomeFilme.replace("Top", "Matrix")}\n"
      f"8 - Quebra a string com o item que foi adicionado como parâmetro: {descricaoFilme.split('a')}\n")

print(linha*50)
print("Forma de saida de resultado sem concatenar")
print(nomeFilme.upper())
print(nomeFilme.lower())
print(nomeFilme.capitalize())
print(nomeFilme.title())
