# lista = {
#     'valor': 5,
#     'proximo': None
# }

lista = None

def exibiLista():

    if not lista:
        print('Lista vazia')
        return

    elemento = lista

    while elemento != None:
        print(f"{elemento['valor']} ", end='')
        elemento = elemento['proximo']
    print('.')


def adicionaNoFim(elemento):
    global lista

    if not lista:
        lista = {'valor': elemento, 'proximo': None}
        return

    atual = lista
    while atual['proximo']:
        atual = atual['proximo']
    atual['proximo'] = {'valor': elemento, 'proximo': None}


exibiLista()
print('Adicionando 5')
adicionaNoFim(5)
exibiLista()
print('Adicionando 10')
adicionaNoFim(10)
exibiLista()
print('Adicionando 15')
adicionaNoFim(15)
exibiLista()

print(lista)