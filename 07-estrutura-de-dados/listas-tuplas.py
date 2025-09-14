# lista = [1, 2, 3, 4]
# tupla = (1, 2, 3, 4)

import os
# Lista de Tarefas
tarefas = []


def adicionaTarefa(tarefa):
    novaTarefa = (tarefa, "pendente")
    tarefas.append(novaTarefa)


def exibeTarefas():
    if not tarefas:
        print('A lista de tarefas está vazia.')
        return

    for tarefa in tarefas:
        print(f'{tarefa[0]} - Status: {tarefa[1]}')


def concluirTarefa(tarefa):
    global tarefas  # tarefas recebe uma lista nova

    tarefas = [(t[0], "concluída") if t[0] == tarefa else t for t in tarefas]


def removerTarefa(tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t[0] != tarefa]


def buscarTarefa(tarefa):
    resultado = [t for t in tarefas if t[0] == tarefa.lower()]

    if len(resultado) > 0:
        for titulo, status in resultado:
            print(f'Encontrada: {titulo} - Status: {status}')
    else:
        print(f'Tarefa não encontrada: {tarefa}')


while True:
    os.system('cls | clear')

    print('Boas Vindas ao gerenciador de tarefas!')
    print()
    print('O que você quer fazer agora?')
    print('1 - Listar tarefas')
    print('2 - Adicionar tarefas')
    print('3 - Remover tarefa')
    print('4 - Marcar tarefa como concluída')
    print('5 - Buscar tarefa')
    print('0 - Sair')

    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            exibeTarefas()
        case 2:
            tarefa = input('Digite o nome da tarefa: ')
            adicionaTarefa(tarefa)
        case 3:
            tarefa = input('Digite o nome da tarefa a ser removida: ')
            removerTarefa(tarefa)
        case 4:
            tarefa = input('Digite o nome da tarefa a ser concluída: ')
            concluirTarefa(tarefa)
        case 5:
            tarefa = input('Digite o nome da tarefa a ser buscada: ')
            buscarTarefa(tarefa)
        case 0:
            break
        case _:
            print('Opção inválida! Tente novamente.')

    print()
    input('Pressione Enter para continuar...')


# adicionaTarefa("Estudar Python")
# adicionaTarefa("Lavar a louça")
# exibeTarefas()
# buscarTarefa("Estudar Python")
# print('Agora vou concluir a tarefa')
# concluirTarefa('Estudar Python')
# concluirTarefa('Ir ao mercado')  # Tarefa não existe
# print('Agora vou remover a tarefa')
# removerTarefa('Estudar Python')
# exibeTarefas()
# buscarTarefa('Arrumar o quarto')

# List comprehension (forma reduzida de criar listas)

# novaLista = [expressão for item in lista if condição]
