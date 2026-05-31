# Função para imprimir uma mensagem
print("\n---- Função para imprimir uma mensagem ----")


def bemvindo():
    print("Bem vindo a primeira mensagem da função!")


bemvindo()

# Se eu quiser repetir a mesma coisa sem duplicar linhas de codigos
print("\n---- Repetindo a mesma coisa sem duplicar linhas de codigos ----")


def bemvindo():
    print("Bem vindo a primeira mensagem da função!")


for i in range(10):
    bemvindo()

# Função para calcular a media de notas

'''
def calcularMedia():

    numeroAvaliacao = int(input('Digite a quantidade de avaliações: \n'))

    total = 0
    for i in range(numeroAvaliacao):
        nota = float(input("Digite o valor da nota: \n"))
        total += nota

    if numeroAvaliacao > 0:
        media = total / numeroAvaliacao

    else:
        media = 0

    return media


print(f"A média de avaliação é: {calcularMedia():.2f}")
'''
# Função para cadastrar um filme
print("\n---- Função para cadastrar um filme ----")


def criarFilme():
    while True:
        nome = input(
            "\nDigite o nome do filme (ou sair para encerrar o programa):\n")
        if nome.lower() == "sair":
            print("\nPrograma encerrado!")
            break
        anoLancamento = int(input("Digite o ano de lançamento: \n"))
        preco = float(input("Digite o preço do filme: \n"))
        nota = float(input("Digite a nota do filme: \n"))

        print(f"{nome} ({anoLancamento}) - R${preco}")


criarFilme()
