import logging

# Configuração do logger para soluções sequenciais
seq_logger = logging.getLogger('seq_logger')
seq_handler = logging.FileHandler('logs/nqueens_solution_sequential.log', encoding='utf-8')
seq_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
seq_logger.setLevel(logging.INFO)
seq_logger.addHandler(seq_handler)

# Configuração do logger para soluções paralelas com processos
par_logger = logging.getLogger('par_logger')
par_handler = logging.FileHandler('logs/nqueens_process_solution_parallel.log', encoding='utf-8')
par_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
par_logger.setLevel(logging.INFO)
par_logger.addHandler(par_handler)

# Configuração do logger para soluções paralelas com threads
thr_logger = logging.getLogger('thr_logger')
thr_handler = logging.FileHandler('logs/nqueens_threads_solution_parallel.log', encoding='utf-8')
thr_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
thr_logger.setLevel(logging.INFO)
thr_logger.addHandler(thr_handler)

def seq_print_board(board, solution_number):
    seq_logger.info("\n")  # Linha em branco antes da solução
    seq_logger.info(f"Solução {solution_number} encontrada:\n")
    board_str = "\n"
    for row in board:
        board_str += " ".join(" ♕ " if cell else " - " for cell in row) + "\n"
    board_str += "\n"
    seq_logger.info(board_str + "\n")  # Linha em branco após a solução

def par_print_board(board, solution_number):
    par_logger.info("\n")  # Linha em branco antes da solução
    par_logger.info(f"Solução {solution_number} encontrada:\n")
    board_str = "\n"
    for row in board:
        board_str += " ".join(" ♕ " if cell else " - " for cell in row) + "\n"
    board_str += "\n"
    par_logger.info(board_str + "\n")  # Linha em branco após a solução

def thr_print_board(board, solution_number):
    thr_logger.info("\n")  # Linha em branco antes da solução
    thr_logger.info(f"Solução {solution_number} encontrada:\n")
    board_str = "\n"
    for row in board:
        board_str += " ".join(" ♕ " if cell else " - " for cell in row) + "\n"
    board_str += "\n"
    thr_logger.info(board_str + "\n")  # Linha em branco após a solução

def seq_print_summary(total_solutions, total_time):
    seq_logger.info("\n")
    seq_logger.info("Resumo da execução:")
    seq_logger.info(f"Total de soluções encontradas: {total_solutions}")
    seq_logger.info(f"Tempo total de execução: {total_time:.2f} segundos")
    seq_logger.info("\n")

def par_print_summary(total_solutions, total_time):
    par_logger.info("\n")
    par_logger.info("Resumo da execução:")
    par_logger.info(f"Total de soluções encontradas: {total_solutions}")
    par_logger.info(f"Tempo total de execução: {total_time:.2f} segundos")
    par_logger.info("\n")

def thr_print_summary(total_solutions, total_time):
    thr_logger.info("\n")
    thr_logger.info("Resumo da execução:")
    thr_logger.info(f"Total de soluções encontradas: {total_solutions}")
    thr_logger.info(f"Tempo total de execução: {total_time:.2f} segundos")
    thr_logger.info("\n")

def clear_logs():
    with open('logs/nqueens_solution_sequential.log', 'w', encoding='utf-8') as seq_file:
        seq_file.write('')  # Limpa o conteúdo do arquivo

    with open('logs/nqueens_process_solution_parallel.log', 'w', encoding='utf-8') as par_file:
        par_file.write('')  # Limpa o conteúdo do arquivo

    with open('logs/nqueens_threads_solution_parallel.log', 'w', encoding='utf-8') as thr_file:
        thr_file.write('')  # Limpa o conteúdo do arquivo