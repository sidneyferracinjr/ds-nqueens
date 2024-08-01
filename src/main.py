import sequential_solver

"""
Dado um tabuleiro de xadrez de N x N, o objetivo é posicionar N rainhas no 
tabuleiro de tal forma que nenhuma rainha possa atacar outra.
Em termos de xadrez, uma rainha pode atacar qualquer outra 
peça que esteja na mesma linha, coluna ou diagonal.
"""

# Altera o tamanho do tabuleiro #
n = 8
# ----------------------------- #

board = [[0] * n for _ in range(n)]
if sequential_solver.solve_nqueens(board, 0):
    sequential_solver.print_board(board)
else:
    print("Não existe solução para o problema das", n, "rainhas.")