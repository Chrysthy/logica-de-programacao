# lista = [1, 2, 3, 4]
# tupla = (1, 2, 3, 4)

# Lista de Tarefas
tarefas = []


def adicionaTarefa(tarefa):
    novaTarefa = (tarefa, "pendente")
    tarefas.append(novaTarefa)


def exibeTarefas():
    for tarefa in tarefas:
        print(f'{tarefa[0]} - Status: {tarefa[1]}')


def concluirTarefa(tarefa):
    global tarefas  # tarefas recebe uma lista nova

    tarefas = [(t[0], "concluída") if t[0] == tarefa else t for t in tarefas]


def removerTarefa(tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t[0] != tarefa]


def buscarTarefa(tarefa):
    resultado = [t for t in tarefas if t[0] != tarefa.lower()]

    if len(resultado) > 0:
        for titulo, status in resultado:
            print(f'Encontrada: {titulo} - Status: {status}')
    else:
        print(f'Tarefa não encontrada: {tarefa}')


adicionaTarefa("Estudar Python")
adicionaTarefa("Lavar a louça")
exibeTarefas()

buscarTarefa("Estudar Python")


# print('Agora vou concluir a tarefa')
# concluirTarefa('Estudar Python')
# concluirTarefa('Ir ao mercado')  # Tarefa não existe
# print('Agora vou remover a tarefa')
# removerTarefa('Estudar Python')
# exibeTarefas()
# buscarTarefa('Arrumar o quarto')

# List comprehension (forma reduzida de criar listas)

# novaLista = [expressão for item in lista if condição]
