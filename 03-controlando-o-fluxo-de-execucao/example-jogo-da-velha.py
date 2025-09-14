tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

jogador = 'X'

#print(tabuleiro)

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


def temGanhador():

    """ Verifica as linhas """
    for linha in range(3):
        if (
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][2]
        ):
            print(f'{tabuleiro[linha][0]} GANHOU!!!')
            return True

    """ Verifica as colunas """
    for coluna in range(3):
        if (
            tabuleiro[0][coluna]!= ' ' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f'{tabuleiro[0][coluna]} GANHOU!!!')
            return True

    """ Verifica as diagonais """
    if (
        tabuleiro[1][1] != ' ' and
        (
            (
                tabuleiro[0][0] == tabuleiro[1][1] and
                tabuleiro[0][0] == tabuleiro[2][2]
            ) or
            (
                tabuleiro[0][2] == tabuleiro[1][1] and
                tabuleiro[1][1] == tabuleiro[2][0]
            )
        )
    ):
            print(f'{tabuleiro[1][1]} GANHOU!!!')
            return True

    """ Se não teve ganhador em nenhuma forma """
    return False

def temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    print('Acabou empatado!')
    return True


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

    if temGanhador() or temEmpate():
        break

    exibirTabuleiro()