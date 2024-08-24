import time
from multiprocessing import Process, Manager
from save_board import par_print_board, par_print_summary

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
            solve_nqueens(board, col + 1, solutions)
            board[row][col] = 0  # Backtracking

def solve_nqueens_parallel(row, n, shared_solutions):
    board = [[0] * n for _ in range(n)]
    if is_position_safe(board, row, 0):
        board[row][0] = 1
        local_solutions = []
        solve_nqueens(board, 1, local_solutions)  # Começa da segunda coluna
        shared_solutions.extend(local_solutions)  # Adiciona as soluções encontradas ao resultado compartilhado

def print_boards(solutions):
    # Imprime todas as soluções encontradas.
    for index, board in enumerate(solutions):
        par_print_board(board, index + 1)  # Passa o número da solução para a função


def main(n):
    # Função principal para resolver o problema das N-rainhas e imprimir todas as soluções.
    start_time = time.time() # Início da medição do tempo
    
    # Usando Manager para criar uma lista compartilhada entre processos
    with Manager() as manager:
        shared_solutions = manager.list()
        processos = []

        # Criar um processo para cada linha inicial da primeira coluna
        for row in range(n):
            p = Process(target=solve_nqueens_parallel, args=(row, n, shared_solutions))
            processos.append(p)
            p.start()

        # Esperar que todos os processos terminem
        for p in processos:
            p.join()

        end_time = time.time() # Fim da medição do tempo

        total_time = end_time - start_time # Tempo total de execução

        print(f"Total de soluções encontradas: {len(shared_solutions)}")
        print(f"Tempo total de execução: {total_time:.2f} segundos\n")
        
        # Imprimir soluções usando a função paralela
        print_boards(shared_solutions)

        par_print_summary(len(shared_solutions), total_time)

# Exemplo de uso:
if __name__ == "__main__":
    main(13) # Substitua 8 pelo tamanho desejado do tabuleiro
