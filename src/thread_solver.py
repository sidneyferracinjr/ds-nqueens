import time
from threading import Thread, Lock
from save_board import thr_print_board, thr_print_summary

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

def solve_nqueens_thread(row, n, shared_solutions, lock):
    board = [[0] * n for _ in range(n)]
    if is_position_safe(board, row, 0):
        board[row][0] = 1
        local_solutions = []
        solve_nqueens(board, 1, local_solutions)  # Começa da segunda coluna
        with lock:  # Bloquear a lista compartilhada para acesso seguro
            shared_solutions.extend(local_solutions)

def print_boards(solutions):
    # Imprime todas as soluções encontradas.
    for index, board in enumerate(solutions):
        thr_print_board(board, index + 1)  # Passa o número da solução para a função

def main(n):
    # Função principal para resolver o problema das N-rainhas e imprimir todas as soluções.
    start_time = time.time() # Início da medição do tempo

    shared_solutions = []
    threads = []
    lock = Lock()  # Lock para sincronizar o acesso à lista compartilhada

    # Criar uma thread para cada linha inicial da primeira coluna
    for row in range(n):
        t = Thread(target=solve_nqueens_thread, args=(row, n, shared_solutions, lock))
        threads.append(t)
        t.start()

    # Esperar que todas as threads terminem
    for t in threads:
        t.join()

    end_time = time.time() # Fim da medição do tempo

    total_time = end_time - start_time # Tempo total de execução

    print(f"Total de soluções encontradas: {len(shared_solutions)}")
    print(f"Tempo total de execução: {total_time:.2f} segundos\n")

    # Imprimir soluções usando a função paralela com threads
    print_boards(shared_solutions)

    thr_print_summary(len(shared_solutions), total_time)

# Exemplo de uso:
if __name__ == "__main__":
    main(14) # Substitua 8 pelo tamanho desejado do tabuleiro