# frase = ' O curso de lógica de programação é muito bom! '
# print(type(frase))

# print(f' Primeira letra:{frase[0]}')  
# print(f' Última letra: {frase[-1]}')
# print(f' Tamanho da frase: {len(frase)} caracteres')
# print()
# print(f' Frase maiúscula: {frase.upper()}')
# print(f' Frase minúscula: {frase.lower()}')
# print()
# print(f'Fatiando: {frase.split()}')
# print(f'Fatiando: {frase.split("a")}')

# print()
# print(f'Frase original: {frase}')
# print(f'Limpando: {frase.strip()}') #tira espaços em branco do início e do fim
# print(f'Tamanho da string limpa: {len(frase.strip())}')

frase = 'O curso de lógica de programação é muito bom!'

def analisadorDeTexto(texto):

    palavras = texto.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)
    num_caracteres_sem_espacos = num_caracteres - texto.count(' ')

    return num_palavras, num_caracteres, num_caracteres_sem_espacos
    
num_p, num_c, num_c_s_e = analisadorDeTexto(frase)
print(f'Num palavras: {num_p}')
print(f'Num caracteres: {num_c}')
print(f'Num caracteres sem espacos: {num_c_s_e}')

