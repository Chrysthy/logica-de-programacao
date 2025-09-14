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
    global tarefas

    tarefas = [(t[0], "concluída") if t[0] == tarefa else t for t in tarefas]


adicionaTarefa("Estudar Python")
adicionaTarefa("Lavar a louça")
exibeTarefas()
print('Agora vou concluir a tarefa')
concluirTarefa('Estudar Python')
exibeTarefas()


# List comprehension (forma reduzida de criar listas)

# novaLista = [expressão for item in lista if condição]
