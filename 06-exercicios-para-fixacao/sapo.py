# N= pedra, nos colchetes jeitos diferentes de pular, resultado da quantidade de jeitos diferentes de pular
# N=1 -> [1] = 1
# N=2 -> [1, 1], [2] = 2
# N=3 -> [1, 1, 1], [1, 2], [2, 1] = 3
# N=4 -> [1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2] = 5
# N=5 -> [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1], [1, 2, 2], [2, 1, 2], [2, 2, 1] = 8

# Sequencia de Fibonacci -> A sequência de Fibonacci é uma sequência de números em que cada número é a soma dos dois anteriores.
# o número de pulos depende da soma dos dois pulos anteriores

# 0 - 1
# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 5
# 5 - 8
# 6 - 13
# 7 - 21
# 8 - 34
# 9 - 55

def contar_caminhos(num_pedras):
    if num_pedras <= 1:
        return 1
    
    else:
        return contar_caminhos(num_pedras - 1) + contar_caminhos(num_pedras - 2)

print(contar_caminhos(6))