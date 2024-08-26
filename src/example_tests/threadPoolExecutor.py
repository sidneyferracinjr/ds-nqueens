import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from save_board import par_print_board, par_print_summary

def is_position_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col):
    solutions = []
    if col >= len(board):
        solutions.append([row[:] for row in board])
        return solutions

    for row in range(len(board)):
        if is_position_safe(board, row, col):
            board[row][col] = 1
            solutions += solve_nqueens(board, col + 1)
            board[row][col] = 0
    return solutions

def solve_nqueens_parallel(row, n):
    board = [[0] * n for _ in range(n)]
    if is_position_safe(board, row, 0):
        board[row][0] = 1
        return solve_nqueens(board, 1)
    return []

def main(n):
    start_time = time.time()
    
    all_solutions = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(solve_nqueens_parallel, row, n) for row in range(n)]
        
        for future in as_completed(futures):
            all_solutions.extend(future.result())

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Total de soluções encontradas: {len(all_solutions)}")
    print(f"Tempo total de execução: {total_time:.2f} segundos\n")

    for index, board in enumerate(all_solutions):
        par_print_board(board, index + 1)

    par_print_summary(len(all_solutions), total_time)

if __name__ == "__main__":
    main(13)
