from mpi4py import MPI
import time
from save_board import print_board, print_summary, par_logger
from solve_utils import is_position_safe, solve_nqueens, print_boards

def solve_nqueens_parallel(row, n):
    board = [[0] * n for _ in range(n)]
    local_solutions = []
    if is_position_safe(board, row, 0):
        board[row][0] = 1
        solve_nqueens(board, 1, local_solutions)  # Começa da segunda coluna
    return local_solutions

def main(n):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()  # Número total de processos

    # O processo 0 imprime o número de núcleos (processos MPI)
    if rank == 0:
        print(f"Numero de nucleos (processos MPI) utilizados: {size}")
    
    start_time = time.time() if rank == 0 else None

    # Cada processo resolve o problema para diferentes linhas iniciais
    local_solutions = []
    for row in range(rank, n, size):
        local_solutions.extend(solve_nqueens_parallel(row, n))

    # Reunir todas as soluções no processo 0
    all_solutions = comm.gather(local_solutions, root=0)

    if rank == 0:
        all_solutions = [sol for sublist in all_solutions for sol in sublist]  # Achatar lista de listas
        end_time = time.time()
        total_time = end_time - start_time

        print(f"Total de soluções encontradas: {len(all_solutions)}")
        print(f"Tempo total de execução: {total_time:.2f} segundos\n")
        
        # Imprimir soluções usando a função genérica
        print_boards(all_solutions, lambda board, index: print_board(board, index, par_logger))

        # Imprime o resumo das soluções
        print_summary(len(all_solutions), total_time, par_logger)

# Exemplo de uso:
if __name__ == "__main__":
    main(12) # Substitua 8 pelo tamanho desejado do tabuleiro
