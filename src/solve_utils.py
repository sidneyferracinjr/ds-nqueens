# Arquivo de utilidade com funções compartilhadas pelos solvers.

def is_position_safe(board, row, col):
    # Verifica se é seguro colocar uma rainha na posição (row, col) do tabuleiro.

    # Verifica a linha à esquerda
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Verifica a diagonal superior esquerda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Verifica a diagonal inferior esquerda
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, solutions):
    # Resolve o problema das N-rainhas usando backtracking e armazena todas as soluções encontradas.
    if col >= len(board):
        # Encontrou uma solução, adicione uma cópia do tabuleiro à lista de soluções
        solutions.append([row[:] for row in board])
        return

    for row in range(len(board)):
        if is_position_safe(board, row, col):
            board[row][col] = 1
            # print(f"Posicionando rainha em ({row}, {col}).")

            solve_nqueens(board, col + 1, solutions)
            board[row][col] = 0  # Backtracking
            # print(f"Removendo rainha de ({row}, {col}) devido a conflito.")

def print_boards(solutions, print_board_function):
    # Função geral, imprime todas as soluções encontradas.
    for index, board in enumerate(solutions):
        print_board_function(board, index + 1)  # Passa o número da solução para a função especificada
