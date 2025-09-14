tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

jogador = 'X'

print(tabuleiro)

def exibirTabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-'*5)


def jogada(linha, coluna):
    if (
        linha < 0 or linha > 2 or    
        coluna < 0 or coluna > 2 or
        tabuleiro[linha][coluna] != ''
    ):
        print('Jogada inválida! Tente novamente.')
        return jogador

    tabuleiro[linha][coluna] = jogador

    return 'O' if jogador == 'X' else 'X'

while True:
    print(f'Jogador da vez: {jogador}')

    try:
        linha = input('Digite a linha (0, 1, 2): ')
        coluna = input('Digite a coluna (0, 1, 2): ')
        jogador = jogada(int(linha), int(coluna))
    except (ValueError):
        print('Entrada inválida! Por favor, digite valores numéricos inteiros entre 0 e 2para linha e coluna.')
    except (IndexError):
        print('Entrada inválida! Por favor, digite valores numéricos inteiros entre 0 e 2para linha e coluna.')

    exibirTabuleiro()