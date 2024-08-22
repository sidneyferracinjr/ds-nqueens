import time
from sequential_solver import solve_nqueens, print_boards
from save_board import seq_print_board, print_summary, clear_logs

"""
Dado um tabuleiro de xadrez de N x N, o objetivo é posicionar N rainhas no 
tabuleiro de tal forma que nenhuma rainha possa atacar outra.
Em termos de xadrez, uma rainha pode atacar qualquer outra peça que esteja na mesma linha, coluna ou diagonal.
"""

def main(n):
    """
    Função principal para resolver o problema das N-rainhas e imprimir todas as soluções.
    """
    # Limpa os logs antigos antes de iniciar uma nova execução
    clear_logs()

    board = [[0] * n for _ in range(n)]
    solutions = []

    # Início da medição do tempo
    start_time = time.time()
    
    # Resolve o problema das N-rainhas
    solve_nqueens(board, 0, solutions)
    
    # Fim da medição do tempo
    end_time = time.time()
    
    total_time = end_time - start_time  # Tempo total de execução

    # Imprime informações de resumo
    print(f"Total de soluções encontradas: {len(solutions)}")
    print(f"Tempo total de execução: {total_time:.2f} segundos\n")
    
    # Imprime as soluções e registra no log
    print_boards(solutions)
    
    # Imprime o resumo das soluções
    print_summary(len(solutions), total_time)

# Exemplo de uso:
if __name__ == "__main__":
    main(8)  # Substitua 8 pelo tamanho desejado do tabuleiro
