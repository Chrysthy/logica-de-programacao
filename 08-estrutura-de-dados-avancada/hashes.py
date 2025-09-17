# Tabelo Hash em Python

nomes = [
    'Chrystine',
    'Ana',
    'Maria',
    'João',
    'Pedro',
    'Carla',
    'Juliana',
    'Adão'
]

tabela_hash = {}

for nome in nomes:
    # qtd = len(nome)
    qtd = nome[0]

    if qtd not in tabela_hash:
        tabela_hash[qtd] = []
    tabela_hash[qtd].append(nome)

print(tabela_hash)

# Outro exemplo:

texto = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua \
\
ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum \
\
sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium totam rem aperiam eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt neque porro quisquam est qui dolorem ipsum quia dolor sit amet consectetur adipisci velit sed quia non numquam eius modi tempora \
\
incidunt ut labore et dolore magnam aliquam quaerat voluptatem ut enim ad minima veniam quis nostrum exercitationem ullam corporis suscipit laboriosam nisi ut aliquid ex ea commodi consequatur quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur vel illum qui dolorem eum fugiat quo voluptas nulla pariatur'

palavras = texto.split()

tabela_hash = {}

for palavra in palavras:
    indice = palavra[0].upper()

    if indice not in tabela_hash:
        tabela_hash[indice] = []
    tabela_hash[indice].append(palavra)

# print(tabela_hash)

for chave, valor in tabela_hash.items():
    print(f'{chave}: {valor}')
    print(f'{chave}: {len(valor)}')

print(len(texto.split()))
# tabela_hash['p']
