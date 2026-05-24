'''
# Exemplo 1
nome = input("Digite o nome do filme: \n")
anoLancamento = int(input("Digite o ano de lançamento: \n"))
notaFilme = float(input("Digite a nota do filme: \n"))

# Verificar se o filme é recomendado
if notaFilme > 8.0 and anoLancamento > 2015:
    print(f"O filme {nome} é muito bom! Recomendo assisti-lo")

else:
    print(f"O filme {nome} ainda não é recomendado!")
'''

# Exemplo 2
num1 = float(input("Digite o primeiro numero: \n"))
num2 = float(input("Digite o segundo numero: \n"))
operacao = input("Digite a operação a ser realizada: (+ - * /)\n")

if operacao == "+":
    result = num1 + num2
elif operacao == "-":
    result = num1 - num2
elif operacao == "*":
    result = num1 * num2
elif operacao == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro na divisão por ZERO")
        result = 0
else:
    print("Operação inválida")
    result = 0

print(f"Resultado da operação é: {result:.2f}")
