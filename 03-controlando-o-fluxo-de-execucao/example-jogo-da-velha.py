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
    tabuleiro[linha][coluna] = jogador

    if jogador == 'X':
        return 'O'
    else: 
        return'X'



jogador = jogada(1,1)
jogador = jogada(1,2)

exibirTabuleiro()