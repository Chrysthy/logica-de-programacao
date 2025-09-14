# Pilhas e Filas

# Pilha (stack) - LIFO (Last In, First Out) - o último a entrar é o primeiro a sair
# Exemplo: pilha de pratos

# Fila (queue) - FIFO (First In, First Out) - o primeiro a entrar é o primeiro a sair
# Exemplo: fila de banco

#fila

from collections import deque

def criaPilha():
    return deque()

def insereNaPilha(fila, elemento):
    fila.append(elemento)


def removeDaPilha(fila):
    return fila.popleft()


pilha = criaPilha()
print(pilha)  # []
insereNaPilha(pilha, '8')
insereNaPilha(pilha, '9')
insereNaPilha(pilha, '10')
insereNaPilha(pilha, '11')
insereNaPilha(pilha, '12')
print(f'Removendo {removeDaPilha(pilha)}')
print(f'Removendo {removeDaPilha(pilha)}')
print(pilha) 


# Pilha

def criaPilha():
    return deque()

def insereNaPilha(pilha, elemento):
    pilha.append(elemento)


def removeDaPilha(pilha):
    return pilha.pop()


pilha = criaPilha()
print(pilha)  # []
insereNaPilha(pilha, '8')
insereNaPilha(pilha, '9')
insereNaPilha(pilha, '10')
insereNaPilha(pilha, '11')
insereNaPilha(pilha, '12')
print(f'Removendo {removeDaPilha(pilha)}')
print(f'Removendo {removeDaPilha(pilha)}')
print(pilha) 