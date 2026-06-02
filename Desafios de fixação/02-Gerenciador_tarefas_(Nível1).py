'''Desafio: Gerenciador de Tarefas(Nível 1)

Este exercício utiliza a mesma estrutura do anterior, mas com uma lógica matemática mais simples.
Escreva um programa com os seguintes requisitos:

1. Menu Principal (while, if/elif/else):
Exiba três opções: 1 - Nova Tarefa, 2 - Buscar Tarefa, 3 - Sair.
O loop só deve quebrar se o usuário escolher a opção 3 ou digitar "sair".

2. Cadastro(input, dicionário, lista):
Crie uma função para adicionar tarefas.
Peça ao usuário o nome da tarefa(string) e a prioridade(string: Alta, Média ou Baixa).
Salve os dados em um dicionário e adicione-o a uma lista global .

3. Busca e Lógica (função, for, if/else):
Crie uma função para buscar a tarefa pelo nome(ignorando maiúsculas/minúsculas).
Se a tarefa for encontrada, exiba os dados.
Adicione a regra: se a prioridade for "Alta" (ou "alta"), imprima também a mensagem: "Atenção: Fazer hoje!". Caso contrário, imprima "Pode esperar.".
Se não encontrar, exiba uma mensagem de erro.
Pode enviar seu código quando terminar. Bom trabalho!
'''

tarefas = []


def cadastro():
    nome = input('Digite a nova tarefa:\n')

    if not nome:
        print('Informe uma tarefa válida!')
        return None

    prioridade = input(
        'Digite a prioridade da tarefa:\n 1 - Alta\n 2 - Media\n 3 - Baixa\n')
    if prioridade == '1':
        prioridade = 'alta'
    elif prioridade == '2':
        prioridade = 'media'
    elif prioridade == '3':
        prioridade = 'baixa'
    else:
        return f'Digite uma opção válida!'

    adicionarTarefas = {
        'nome': nome,
        'prioridade': prioridade
    }

    tarefas.append(adicionarTarefas)

    return f'A tarefa {nome} com prioridade {prioridade} foi adicionada com sucesso!'


def buscar():
    procurarTarefa = input(
        'Digite a opção que deseja usar:\n 1 - Digitar o nome da tarefa\n 2 - Mostrar todas as tarefas\n')
    if procurarTarefa == '1':
        nomeTarefa = input('Digite o nome da tarefa:\n')
        buscarTarefa = [tarefa for tarefa in tarefas if nomeTarefa.lower(
        ) == tarefa['nome'].lower()]

        if buscarTarefa:

            tarefaDados = buscarTarefa[0]
            prioridade = tarefaDados['prioridade']

            if prioridade == 'alta':
                status = 'Atenção: Fazer hoje!'
            else:
                status = 'Pode esperar.'

            print(
                f'A tarefa {tarefaDados['nome']} foi encontrada e tem prioridade {prioridade} com status {status}')
        else:
            print(f'A tarefa {nomeTarefa} não foi encontrado!')
    elif procurarTarefa == '2':

        if not tarefas:
            return 'Não há tarefas'

        print('\n--- TODAS AS TAREFAS ---')
        for tarefa in tarefas:

            tarefaDados2 = tarefa['nome']
            prioridade = tarefa['prioridade']

            if prioridade == 'alta':
                status = 'Atenção: Fazer hoje!'
            else:
                status = 'Pode esperar.'

            print(
                f'Tarefa: {tarefaDados2} | Prioridade: {prioridade} | Status: {status}')

    return 'Fim da listagem'


while True:
    menu = (input(
        'Digite uma opção válida:\n 1 - Nova tarefa\n 2 - Buscar tarefa\n 3 - Sair\n'))
    if menu == '1':
        print(cadastro())
    elif menu == '2':
        print(buscar())
    elif menu.lower() == '3' or menu == 'sair':
        print('Programa encerrado!')
        break
    else:
        print('Digite uma opção válida!')
