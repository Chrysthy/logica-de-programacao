# Se eu jogar dois dados 1000 vezes, quantas vezes dar[a a soma 7?

import random # gerar numeros aleatorios

numero_de_vezes = 0

for _ in range (1000):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    soma = dado1 + dado2
    if soma == 7 or soma == 11:
        numero_de_vezes += 1
    
print(f'A soma deu 7 um total de {numero_de_vezes} vezes')