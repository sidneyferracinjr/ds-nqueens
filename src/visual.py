import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Define códigos de cores
white_color_code = 0  # Branco para as casas
black_color_code = 1  # Preto para as casas
queen_color_code = 2  # Código para a rainha (vermelho)

def draw_board(ax, board):
    # Cria a matriz de valores numéricos
    color_matrix = np.zeros((len(board), len(board)))

    # Alterna as cores do tabuleiro
    for i in range(len(board)):
        for j in range(len(board)):
            if (i + j) % 2 == 0:
                color_matrix[i, j] = white_color_code
            else:
                color_matrix[i, j] = black_color_code

    # Adiciona as rainhas ao tabuleiro
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell:
                color_matrix[i, j] = queen_color_code

    # Define o colormap
    cmap = mcolors.ListedColormap(['white', 'black', 'red'])  # Branco para casas, preto para casas, vermelho para rainhas

    # Configura o gráfico
    cax = ax.imshow(color_matrix, cmap=cmap, interpolation='none')
    ax.set_xticks(np.arange(len(board)))
    ax.set_yticks(np.arange(len(board)))
    ax.set_xticks(np.arange(len(board)+1)-.5, minor=True)
    ax.set_yticks(np.arange(len(board)+1)-.5, minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])

    # Inverter o eixo y para que (0,0) esteja no topo esquerdo
    ax.invert_yaxis()

def plot_results(sequential_board, parallel_board, seq_time, par_time):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # Ajuste para 1 linha e 2 colunas

    # Desenha os tabuleiros
    draw_board(axs[0], sequential_board)
    axs[0].set_title('Sequencial - Tempo: ' + str(seq_time))

    draw_board(axs[1], parallel_board)
    axs[1].set_title('Paralelo - Tempo: ' + str(par_time))

    plt.tight_layout()
    plt.show()

# Exemplo de uso
sequential_board = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

parallel_board = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Tempo de execução (exemplo)
seq_time = 0.1234
par_time = 0.5678

plot_results(sequential_board, parallel_board, seq_time, par_time)
