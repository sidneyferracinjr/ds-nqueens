import time
import psutil
from save_board import print_board, print_summary, seq_logger
from solve_utils import solve_nqueens, print_boards

def main(n):
    # Função principal para resolver o problema das N-rainhas e imprimir todas as soluções.
    board = [[0] * n for _ in range(n)]
    solutions = []

    start_time = time.time()  # Início da medição do tempo
    start_memory = psutil.Process().memory_info().rss  # Memória inicial

    solve_nqueens(board, 0, solutions)

    end_time = time.time()  # Fim da medição do tempo
    end_memory = psutil.Process().memory_info().rss  # Memória final

    total_time = end_time - start_time  # Tempo total de execução
    memory_used = (end_memory - start_memory) / (1024 ** 2)  # Memória utilizada em MB

    print(f"Total de soluções encontradas: {len(solutions)}")
    print(f"Tempo total de execução: {total_time:.2f} segundos")
    print(f"Memória utilizada: {memory_used:.2f} MB\n")
    
    # Imprimir soluções usando a função genérica
    print_boards(solutions, lambda board, index: print_board(board, index, seq_logger))

    # Imprime o resumo das soluções
    print_summary(len(solutions), total_time, seq_logger)

# Exemplo de uso:
if __name__ == "__main__":
    main(8)  # Substitua 8 pelo tamanho desejado do tabuleiro