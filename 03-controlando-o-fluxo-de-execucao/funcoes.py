# Def é a palavra reservada para definir uma função em Python
def olaMundo():
    print("Olá, mundo!")

olaMundo()

def olaPessoa(nome):
    print(f'Olá, {nome}!')

olaPessoa('Chrys')  # Passando o argumento 'Chrys' para a função olaPessoa

def dobro(numero):
    return numero * 2

dobro(5) # A função retorna 10, mas não estamos fazendo nada com esse valor
print(dobro(5) + 2) # Agora estamos imprimindo o valor retornado pela função

def multiplicaDoisNumero(a, b = 2): # b tem um valor padrão de 2 caso não seja passado um segundo valor
    return a * b

print(multiplicaDoisNumero(3, 6)) 
print(multiplicaDoisNumero(3)) 

"""Essas 3 aspas duplas são usadas para criar comentários de múltiplas linhas ou docstrings (string de documentação), que são usadas para documentar funções."""

# Escopo de código
x = 5
def soma ():
    x = 10
    print(x)
    return x + 1
soma()
print(x)  # x fora da função permanece 5

# Mas se eu não declarar o x dentro da função, ele vai usar o x de fora