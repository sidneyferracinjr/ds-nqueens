import time
import psutil
from threading import Thread, Lock
from save_board import print_board, print_summary, thr_logger
from solve_utils import is_position_safe, solve_nqueens, print_boards

def solve_nqueens_thread(row, n, shared_solutions, lock):
    board = [[0] * n for _ in range(n)]
    if is_position_safe(board, row, 0):
        board[row][0] = 1
        local_solutions = []
        solve_nqueens(board, 1, local_solutions)  # Começa da segunda coluna
        with lock:  # Bloquear a lista compartilhada para acesso seguro
            shared_solutions.extend(local_solutions)

def main(n):
    # Função principal para resolver o problema das N-rainhas e imprimir todas as soluções.
    start_time = time.time() # Início da medição do tempo
    start_memory = psutil.Process().memory_info().rss  # Memória inicial

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
    end_memory = psutil.Process().memory_info().rss  # Memória final

    memory_used = (end_memory - start_memory) / (1024 ** 2)  # Memória utilizada em MB
    total_time = end_time - start_time # Tempo total de execução

    print(f"Total de soluções encontradas: {len(shared_solutions)}")
    print(f"Tempo total de execução: {total_time:.2f} segundos\n")
    print(f"Memória utilizada: {memory_used:.2f} MB\n")
    
    # Imprimir soluções usando a função genérica
    print_boards(shared_solutions, lambda board, index: print_board(board, index, thr_logger))

    # Imprime o resumo das soluções
    print_summary(len(shared_solutions), total_time, thr_logger)

# Exemplo de uso:
if __name__ == "__main__":
    main(12) # Substitua 8 pelo tamanho desejado do tabuleiro