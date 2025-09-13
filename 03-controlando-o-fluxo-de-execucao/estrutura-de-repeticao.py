soma = 0
n = 1

# Uso o while quando não sei quantas vezes vou precisar repetir o bloco de código
# while n <=10:
#     soma = soma + n
#     n = n + 1
#     print(f'Soma: {soma}') 
#     print(f'n: {n}')
#     #O f antes das aspas indica que é uma f-string (string formatada). Ela permite inserir valores de variáveis diretamente dentro da string usando {}.

# print(f'A soma dos 10 primeiros números é {soma}')

# Uso o for quando sei exatamente quantas vezes vou precisar repetir o bloco de código
for index in range(1,11):
    print(index)
    soma = soma + index #soma += index

print(f'A soma dos 10 primeiros números é {soma}')

# soma = sum([i for i in range(1,11)])