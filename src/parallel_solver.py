import time
from multiprocessing import Process, Manager
from save_board import print_board, print_summary, par_logger
from solve_utils import is_position_safe, solve_nqueens, print_boards

def solve_nqueens_parallel(row, n, shared_solutions):
    board = [[0] * n for _ in range(n)]
    if is_position_safe(board, row, 0):
        board[row][0] = 1
        local_solutions = []
        solve_nqueens(board, 1, local_solutions)  # Começa da segunda coluna
        shared_solutions.extend(local_solutions)  # Adiciona as soluções encontradas ao resultado compartilhado

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
        
        # Imprimir soluções usando a função genérica
        print_boards(shared_solutions, lambda board, index: print_board(board, index, par_logger))

        # Imprime o resumo das soluções
        print_summary(len(shared_solutions), total_time, par_logger)

# Exemplo de uso:
if __name__ == "__main__":
    main(8) # Substitua 8 pelo tamanho desejado do tabuleiro
