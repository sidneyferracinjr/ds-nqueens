import time
import psutil
from multiprocessing import Process, Manager
from save_board import print_board, print_summary, par_logger
from solve_utils import is_position_safe, solve_nqueens, print_boards

def solve_nqueens_parallel(row, n, shared_solutions):
    board = [[0] * n for _ in range(n)]
    if is_position_safe(board, row, 0):
        board[row][0] = 1
        local_solutions = []
        solve_nqueens(board, 1, local_solutions)
        shared_solutions.extend(local_solutions)

def main(n):
    start_time = time.time()  # Início da medição do tempo
    start_memory = psutil.Process().memory_info().rss  # Memória inicial

    with Manager() as manager:
        shared_solutions = manager.list()
        processos = []

        for row in range(n):
            p = Process(target=solve_nqueens_parallel, args=(row, n, shared_solutions))
            processos.append(p)
            p.start()

        for p in processos:
            p.join()

        end_time = time.time()  # Fim da medição do tempo
        end_memory = psutil.Process().memory_info().rss  # Memória final

        total_time = end_time - start_time  # Tempo total de execução
        memory_used = (end_memory - start_memory) / (1024 ** 2)  # Memória utilizada em MB

        print(f"Total de soluções encontradas: {len(shared_solutions)}")
        print(f"Tempo total de execução: {total_time:.2f} segundos")
        print(f"Memória utilizada: {memory_used:.2f} MB\n")

        print_boards(shared_solutions, lambda board, index: print_board(board, index, par_logger))
        print_summary(len(shared_solutions), total_time, par_logger)

# Exemplo de uso:
if __name__ == "__main__":
    main(12)  # Substitua 8 pelo tamanho desejado do tabuleiro