# Heap: Fila de prioridades onde colocamos os elementos em formato de pares duplas e vamos ter a prioridade e o que estou colocando na fila.

from heapq import *

fila_prioridades = []

heappush(fila_prioridades, (2, 'Atender cliente VIP'))
heappush(fila_prioridades, (1, 'Situação crítica'))
heappush(fila_prioridades, (3, 'Responder email'))
heappush(fila_prioridades, (1, 'Apagar incêndio'))


while fila_prioridades:
    prioridade, tarefa = heappop(fila_prioridades)

    print(f'Executando: {tarefa} - Prioridade: {prioridade}')
