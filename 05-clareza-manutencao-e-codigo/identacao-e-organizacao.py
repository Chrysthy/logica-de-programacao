def saudacao(nome):
    """
    Gera uma saudação personalizada com um nome.

    Parâmetros:
    nome (str): Nome da pessoa.

    Retorna:
    str: Mensagem de saudação.
    """

    print("Oi")
    return f'Olá, {nome}!'

# Para saber o que a função faz, use o help
help(saudacao)

# É bom colocar um comentário as vezes


def outraFuncao():
    print("Oi")


print(saudacao("Chrys"))


def calcular_soma(num1, num2):
    return num1 + num2


print(calcular_soma(2, 3))
