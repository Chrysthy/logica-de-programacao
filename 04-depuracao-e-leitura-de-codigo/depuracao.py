# Erro léxico = escrever palavra errada
# defi soma(a,b):
#     return a + b
# print(soma(2,3))

# Erro sintático = esquecer de colocar algo ou colocar algo no lugar errado
# def (a,b)soma:
#     return a + b
# print(soma(2,3))

# Erro semântico = o código está correto, mas o resultado não é o esperado
def soma(a,b):
    return a - b
print(soma(2,3))