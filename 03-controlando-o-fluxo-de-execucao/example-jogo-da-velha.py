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
    if tabuleiro [linha][coluna != '']:
        print('Jogada inválida! Tente novamente.')
        return jogador

    tabuleiro[linha][coluna] = jogador

    return 'O' if jogador == 'X' else 'X'

while True:
    print(f'Jogador da vez: {jogador}')

    linha = input('Digite a linha (0, 1, 2): ')
    coluna = input('Digite a coluna (0, 1, 2): ')
    jogador = jogada(int(linha), int(coluna))

    exibirTabuleiro()