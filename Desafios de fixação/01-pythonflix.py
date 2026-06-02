"""
    Desafio: Sistema Pythonflix (Nível 1)

Escreva um programa que atenda aos seguintes requisitos:
Menu Principal (while e if/elif/else):
Crie um loop contínuo que exiba três opções: 1 - Cadastrar Filme, 2 - Buscar Filme, 3 - Sair.
O programa só deve ser encerrado se o usuário digitar a opção 3 ou a palavra "sair".
Cadastro (função, input, dicionário, lista):
Crie uma função para cadastrar filmes.
Peça ao usuário o nome (string), o ano (int) e a nota (float).
Armazene esses dados em um dicionário e adicione esse dicionário a uma lista global de filmes.
Busca (função, list comprehension ou for, métodos de string):
Crie uma função para buscar filmes pelo nome.
Solicite o nome do filme e faça a busca na lista, ignorando se o usuário digitou maiúsculas ou minúsculas (use .lower()).
Exibição e Lógica (f-strings, if/else):
Se o filme for encontrado, exiba os dados formatados na tela.
Adicione uma regra: se a nota for maior ou igual a 8.0, imprima também "Filme Recomendado!". Caso contrário, imprima "Filme regular.".
    """

filmes = []


def cadastrarFilme():
    nome = input(
        "\nDigite o nome do filme que deseja cadastrar:\n")

    if not nome:
        print('Digite um nome valido!')
        return None

    ano = int(input("Digite o ano do filme:\n"))
    avaliacao = float(input("Digite a nota do filme:\n"))

    listaFilme = {
        'nome': nome,
        'ano': ano,
        'avaliacao': avaliacao
    }
    filmes.append(listaFilme)

    return f'Filme {nome} adicionado com sucesso!'


def buscandoFilme():
    nome = input('Informe o nome do filme:\n')

    if not nome:
        print('Digite um nome valido!')
        return None

    filmeEncontrao = [filme
                      for filme in filmes if nome.lower() == filme['nome'].lower()]

    if filmeEncontrao:

        filmesDados = filmeEncontrao[0]
        ano = filmesDados['ano']
        nota = filmesDados['avaliacao']

        if nota >= 8:
            status = 'Filme recomendado'
        else:
            status = 'Filme regular'

        return f'Filme {nome} {ano} esta disponível com nota {nota} e com status de {status}!'
    else:
        return f'O filme {nome.lower()} não está disponível!'


while True:
    menu = (input(
        "Digite uma das 3 opções:\n 1 - Cadastrar filme\n 2 - Buscar filme\n 3 - Sair\n"))
    if menu == '1':
        print(cadastrarFilme())
    elif menu == '2':
        print(buscandoFilme())
    elif menu == '3' or menu.lower() == 'sair':
        print("Programa encerrado!")
        break
    else:
        print('Opção invalida!')
