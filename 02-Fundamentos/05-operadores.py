num1 = int(input("Digite o primeiro numero: \n"))
num2 = int(input("Digite o segundo numero: \n"))

# Aritmétrico
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mul = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"A soma do número {num1} por {num2} são {sum}")
print(f"A subtração do número {num1} por {num2} são {sub}")
print(f"A divisão do número {num1} por {num2} são {div}")
print(f"A multiplicação do número {num1} por {num2} são {mul}")
print(f"O resto da divisão do número {num1} por {num2} são {mod}")
print(f"A exponenciação do número {num1} por {num2} são {exp}")

# Comparação

maior = num1 > num2
menor = num1 < num2
igual = num1 == num2
dif = num1 != num2
maiorIgual = num1 >= num2
menorIgual = num1 <= num2

print(f"Os números {num1} e {num2} são iguais?")
print(f"O número {num1} é maior ou igual a {num2}?")

print(maior)
print(menor)
print(igual)
print(dif)

# Atribuição
num1 += 1  # num1 = num1 + 1
num1 -= 1  # num1 = num1 - 1
num1 *= 1  # num1 = num1 * 1
num1 /= 1  # num1 = num1 / 1
