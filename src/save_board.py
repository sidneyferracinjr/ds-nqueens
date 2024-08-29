import logging

def setup_logger(name, log_file):
    """
    Configura um logger com um nome específico e arquivo de log.
    """
    logger = logging.getLogger(name)
    handler = logging.FileHandler(log_file, encoding='utf-8')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger

# Prepara loggers específicos para cada solver
seq_logger = setup_logger('seq_logger', 'logs/nqueens_solution_sequential.log')
par_logger = setup_logger('par_logger', 'logs/nqueens_process_solution_parallel.log')
thr_logger = setup_logger('thr_logger', 'logs/nqueens_threads_solution_parallel.log')

def print_board(board, solution_number, logger):
    """
    Imprime o tabuleiro da solução usando o logger fornecido.
    """
    logger.info("\n")  # Linha em branco antes da solução
    logger.info(f"Solução {solution_number} encontrada:\n")
    board_str = "\n"
    for row in board:
        board_str += " ".join(" ♕ " if cell else " - " for cell in row) + "\n"
    board_str += "\n"
    logger.info(board_str + "\n")  # Linha em branco após a solução

def print_summary(total_solutions, total_time, logger):
    """
    Imprime o resumo da execução usando o logger fornecido.
    """
    logger.info("\n")
    logger.info("Resumo da execução:")
    logger.info(f"Total de soluções encontradas: {total_solutions}")
    logger.info(f"Tempo total de execução: {total_time:.2f} segundos")
    logger.info("\n")

def clear_logs():
    """
    Limpa os logs antigos para cada tipo de solver.
    """
    with open('logs/nqueens_solution_sequential.log', 'w', encoding='utf-8') as seq_file:
        seq_file.write('')  # Limpa o conteúdo do arquivo

    with open('logs/nqueens_process_solution_parallel.log', 'w', encoding='utf-8') as par_file:
        par_file.write('')  # Limpa o conteúdo do arquivo

    with open('logs/nqueens_threads_solution_parallel.log', 'w', encoding='utf-8') as thr_file:
        thr_file.write('')  # Limpa o conteúdo do arquivo
