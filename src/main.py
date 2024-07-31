"""Solução Sequencial"""

def is_position_safe(board, row, col):
    # Verifica se é seguro colocar uma rainha na posição (row, col) do tabuleiro.

    # Parâmetros:
    # board (list): Matriz 2D representando o tabuleiro.
    # row (int): Linha do tabuleiro.
    # col (int): Coluna do tabuleiro.

    # Retorna:
    # bool: True se for seguro colocar a rainha, False caso contrário.

    # Verificar linha à esquerda
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Verificar diagonal superior esquerda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Verificar diagonal inferior esquerda
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col):
    # Resolve o problema das N-rainhas usando backtracking.

    # Parâmetros:
    # board (list): Matriz 2D representando o tabuleiro.
    # col (int): Coluna atual para posicionar a rainha.

    # Retorna:
    # bool: True se uma solução for encontrada, False caso contrário.

    if col >= len(board):
        return True

    for row in range(len(board)):
        if is_position_safe(board, row, col):
            board[row][col] = 1
            print(f"Posicionando rainha em ({row}, {col}).")

            if solve_nqueens(board, col + 1):
                return True

            # Backtracking: remover a rainha e tentar outra posição
            board[row][col] = 0
            print(f"Removendo rainha de ({row}, {col}) devido a conflito.")

    return False


def print_board(board):
    # Imprime o tabuleiro de forma amigável.

    # Parâmetros:
    # board (list): Matriz 2D representando o tabuleiro.

    print("Solução encontrada:\n")
    for row in board:
        print(" ".join(" ♕ " if cell else " . " for cell in row))
    print()


# Tamanho do tabuleiro
n = 8
board = [[0] * n for _ in range(n)]

if solve_nqueens(board, 0):
    print_board(board)
else:
    print("Não existe solução para o problema das", n, "rainhas.")