# Função para imprimir o nome completo
print("\n--- Função para imprimir o nome completo ---")


def nome_completo(primeiroNome, ultimoNome):
    print(f"O nome completo é: {primeiroNome} {ultimoNome}")


nome_completo('Luiz', 'Pedrosa')

# Função de soma
print('\n--- Função de soma ---')


def somaNumero(a, b):
    return a + b


print(f"A soma é: {somaNumero(10, 50)}")

# função com parâmetro default
print("\n--- função com parâmetro default ---")


def endereço(pais="Brasil"):
    print(f'Eu moro no {pais}')


endereço()  # retorna a linha dentro da função
endereço('Portugal')  # Altera a resposta padrão da função

# Função para avaliar filme
print("\n--- Função para avaliar filme ---")


def avaliacaoFilme(nomeFilme, avaliacaoFilme):
    total = 0
    for i in range(avaliacaoFilme):
        nota = float(input("Digite a nota do filme:\n"))
        total += nota

    if avaliacaoFilme > 0:
        media = total / avaliacaoFilme
    else:
        media = 0

    print(
        f'A média de avaliação do filme {nomeFilme} é {media:.2f}')


avaliacaoFilme('Harry Potter', 3)
