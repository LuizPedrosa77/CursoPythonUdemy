'''
A função lambda em Python é uma pequena função anônima. 
Diferente de uma função tradicional definida com def, 
ela não possui um nome e é escrita em uma única linha, 
sendo ideal para operações simples e rápidas que serão usadas uma única vez.
'''
linha = '='
# Função de potência de um número

soma = lambda num: num ** 2

print(soma(5))
print(linha * 50)
# verifica se é par

numPar = lambda x: x % 2 == 0
print(numPar(998))
print(linha * 50)
# Função de divisão
divisao = lambda x, y: x / y
print(f'{divisao(100, 60):.2f}')
print(linha * 50)
# Função que reverte uma string
reverteString = lambda s: s[::-1]
print(reverteString('Luiz'))
