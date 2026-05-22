linha = "="

# Ex1 - Colocando o segundo nome antes do primeiro
# primeiroNome = input("Digite o primeiro nome:\n")
# segundoNome = input("Digite o segundo nome:\n")

# nomeFormatado = f"{segundoNome} {primeiroNome}"

# print(nomeFormatado)

print(linha*50)

# Ex2 - invertendo o texto de trás para frente
texto = "Python é muito interessante"
palavras = texto.split()
textoInvertido = " ".join(palavras[::-1])
print(textoInvertido)

print(linha*50)

# Ex3 -
texto1 = "arara"
texto2 = "Python"
'''transformando texto em minusculo e retirando espaços invisíveis'''
textoFormatado2 = texto1.lower().replace(" ", "")
textoFormatado3 = texto2.lower().replace(" ", "")
'''comparando se o texto de trás para frente é igual ao texto normal'''
palidromo1 = textoFormatado2 == texto1[::-1]
palidromo2 = textoFormatado3 == texto1[::-1]

print(palidromo1)
print(palidromo2)
