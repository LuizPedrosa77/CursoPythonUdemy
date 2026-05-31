'''
Fatorial de um número:
1 -> 1 * 1
2 -> 1 * 2
3 -> 1 * 2 * 3
'''
# Fatorial de um numero


def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num - 1))


numero = int(input("Digite um número para fatorial:\n"))
print(f'O fatorial de {numero} é: {fatorial(numero)}')


# Soma total de um número
def somaTotal(num):
    if num == 1:
        return 1
    else:
        return (num + somaTotal(num - 1))


numero = int(input("Digite um número para somar:\n"))
print(f'A soma total do {numero} é: {somaTotal(numero)}')
