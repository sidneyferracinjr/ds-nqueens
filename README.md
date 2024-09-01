<p align="center">
  <img src="https://img.freepik.com/fotos-premium/xadrez-do-rei-closeup-em-pe-sobre-os-conceitos-de-xadrez-caindo-de-vitoria_101448-4111.jpg" alt="Logo do Projeto">
</p>

<div align="center">
  <h1>👑 O Problema das N Rainhas 👑</h1>
  <h3>Projeto da disciplina de Sistemas Distribuídos</h3>
  <p>Este projeto implementa diferentes abordagens para resolver o problema das N-Rainhas, utilizando programação sequencial, paralela e distribuída. O problema das N-Rainhas consiste em posicionar N rainhas em um tabuleiro NxN de modo que nenhuma rainha ataque a outra.</p>
</div>
<div>

<h3>🤝 Contribuidores</h3>
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/0nMarvin">
        <img src="https://avatars.githubusercontent.com/u/153041241?v=4" width="100px;" alt="0nMarvin"/><br>
        <sub>
          <b>0nMarvin</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/douglas-prado1997">
        <img src="https://avatars.githubusercontent.com/u/48699170?v=4" width="100px;" alt="douglas-prado1997"/><br>
        <sub>
          <b>douglas-prado1997</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/hebertwilly">
        <img src="https://avatars.githubusercontent.com/u/77469709?v=4" width="100px;" alt="hebertwilly"/><br>
        <sub>
          <b>hebertwilly</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/jwvIyx">
        <img src="https://avatars.githubusercontent.com/u/85976926?v=4" width="100px;" alt="jwvIyx"/><br>
        <sub>
          <b>jwvIyx</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/LCostaF">
        <img src="https://avatars.githubusercontent.com/u/146568540?v=4" width="100px;" alt="LCostaF"/><br>
        <sub>
          <b>LCostaF</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Mei0-Metr0">
        <img src="https://avatars.githubusercontent.com/u/163468366?v=4" width="100px;" alt="Mei0-Metr0"/><br>
        <sub>
          <b>Mei0-Metr0</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/sidneyferracinjr">
        <img src="https://avatars.githubusercontent.com/u/176786424?v=4" width="100px;" alt="sidneyferracinjr"/><br>
        <sub>
          <b>sidneyferracinjr</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
</div>

## Repositório Git do projeto

<a href="[text](https://github.com/sidneyferracinjr/ds-nqueens)">

## Estrutura do Projeto

- `src/`
  - `example_tests/`: Contém implementações de exemplos de testes utilizando outras abordagens.
    - `processPoolExecutor.py`: Solução paralela usando `ProcessPoolExecutor`.
    - `threadPoolExecutor.py`: Solução concorrente usando `ThreadPoolExecutor`.
    - `distributed_solver.py`: Solução distribuída usando `mpi4py` para resolver o problema das N-rainhas.
  - `main.py`: Executa todas as implementações (sequencial, paralela) para comparação.
  - `sequential_solver.py`: Implementação da solução sequencial para o problema das N-Rainhas.
  - `parallel_solver.py`: Implementação da solução paralela usando multiprocessing.
  - `thread_solver.py`: Solução concorrente usando threads da biblioteca `threading`.
  - `save_board.py`: Contém funções para salvar o resultado das soluções e configuradores de logger.
  - `solve_utils.py`: Contém funções utilitárias comuns usadas por todas as implementações.
- `README.md`: Documentação do projeto.

## Requisitos

- Python
- `mpi4py` (para a solução distribuída)
- `concurrent.futures` (para `ProcessPoolExecutor` e `ThreadPoolExecutor`)
- `psutil` (para monitoramento de memória)
- `logging` (para registro das soluções)

## Como executar

1. Instale as dependências necessárias:
  - `pip install mpi4py psutil`

2. Executando a solução paralela, sequencial e thread de uma vez:
  - `python src/main.py` ou `src/python3 main.py` (dependendo da versão python instalada).

3. Como compilar e executar apenas a solução sequencial:
  - `python src/sequential_solver.py`

4. Como compilar e executar  apenas a solução paralela com processos:
  - `python src/parallel_solver.py`

5. Como compilar e executar apenas a solução paralela com threads:
  - `python src/thread_solver.py`

## Implementação

1. Solução sequencial:
  - Utiliza uma abordagem de backtracking padrão para encontrar todas as soluções possíveis para o problema das N-rainhas.
  - O tempo de execução e memória utilizada é medido e todas as soluções são registradas em um arquivo de log.

2. Solução Paralela utilizando processos:
 - Utiliza a biblioteca multiprocessing para criar um processo para cada linha inicial da primeira coluna.
 - Todas as soluções encontradas são combinadas usando uma lista gerenciada compartilhada.

3. Solução Paralela utilizando threads:
 - Utiliza a biblioteca threading para criar uma thread para cada linha inicial da primeira coluna.
 - Utiliza um Lock para sincronizar o acesso à lista de soluções compartilhadas.

## Logs e visualização

**Cada solução imprime o resultado no console e também registra os resultados em arquivos de log localizados na pasta logs/. Os arquivos de log incluem:**
  
  - `nqueens_solution_sequential.log`
  - `nqueens_process_solution_parallel.log`
  - `nqueens_threads_solution_parallel.log`

**Para as três soluções é medido o tempo total de execução e o consumo de memória em MB da maquina**

## Comparação de Desempenho

 - O grupo testou a solução sequencial em diferentes tamanhos de N para obter uma linha de base e comparar o tempo de execução com a solução paralela/distribuída. Os testes foram realizados nas seguintes configurações de máquina:

  - **Configuração da maquina testada**
    - Intel® Core™ i3-6006U CPU @ 2.00GHz × 4
    - 4GB de memória ram
    - Python 3.10.12
 
  - **Testes sequenciais**
    - 8 rainhas: 
        Total de soluções encontradas: 92
        Tempo total de execução: 0.02 segundos
        Memória utilizada: 0.12 MB
  
    - 12 rainhas:
        Total de soluções encontradas: 14200
        Tempo total de execução: 14.79 segundos
        Memória utilizada: 29.00 MB

  - **Testes paralelos (processos)**
    - 8 rainhas:
        Total de soluções encontradas: 92
        Tempo total de execução: 0.39 segundos
        Memória utilizada: 3.88 MB
    
    - 12 rainhas:
        Total de soluções encontradas: 14200
        Tempo total de execução: 8.18 segundos
        Memória utilizada: 4.25 MB
  
  - **Testes paralelos (threads)**
    - 8 rainhas:
        Total de soluções encontradas: 92
        Tempo total de execução: 0.03 segundos
        Memória utilizada: 0.38 MB

    - 12 rainhas:
        Total de soluções encontradas: 14200
        Tempo total de execução: 17.51 segundos
        Memória utilizada: 29.38 MB

  - A análise dos resultados mostra que, conforme o número de rainhas aumenta, a solução `parallel_solver.py` se torna significativamente mais eficiente em termos de tempo de execução comparado à solução sequencial. Isso se deve à capacidade de dividir o problema em subproblemas menores que podem ser resolvidos simultaneamente em múltiplos núcleos de processamento. Para números menores de rainhas a solução `sequential_solver.py` mostra-se com certa eficiência, pois em uma quantidade maior o modelo tem menos casos de teste para realizar, já que esse modelo testa massivamente todas as posições do tabuleiro uma a uma.

  - Nota-se também que a solução `thread_solver.py` quando executada com um número maior de rainhas acaba sendo menos eficiente levando um tempo maior de execução e utilizando mais memória que a solução `parallel_solver.py`. Uma das explicações para ocorrer isso é que threads em python tem algumas peculiaridades e problemas que deve ser tratados de formas especificas e para casos com a lógica envolvida no problema das N rainhas acaba tendo uma menor performance pois, no Python, o GIL é um mecanismo que garante que apenas uma thread execute código Python de cada vez, mesmo em sistemas com múltiplos núcleos, isso o torna quase um modelo sequencial, e isso pode limitar a eficácia de threads para tarefas que são CPU-bound (como a resolução do problema das N-rainhas). Dessa forma trabalhar com processos para tarefas CPU-bound em python acaba tendo mais performance.

  - **Gargalos Identificados:**
    - Overhead de comunicação entre processos em soluções paralelas.
    - Na maquina testada (configurações da maquina na sessão "configurações da maquina testada") a partir de 16 rainhas ja ocorre um gargalo e fica quase impossível de receber os resultados.
    - Limitações de paralelismo devido ao número de núcleos disponíveis.
 
  - **Possíveis Melhorias:**
    - Implementação de algoritmos de balanceamento de carga para otimizar o uso de threads.
    - Uso de bibliotecas de baixo nível para reduzir o overhead de comunicação entre processos.
    - Adotar uma abordagem híbrida que combine paralelismo de dados e de tarefas.

 - O tempo de execução e uso de memória pode variar conforme a configuração da maquina mas idependente da configuração a solução `parallel_solver.py` se mostra mais eficiente que as soluções `sequential_solver;py` e `thread_solver.py` para números maiores de rainhas, e as soluções sequencial e paralela com threads se mostram eficiente para números menores de rainhas.

 ## Conclusão

 - Este projeto demonstrou como a paralelização pode melhorar o desempenho na resolução do problema das N-Rainhas. Identificamos que, para tamanhos maiores de tabuleiros, a solução paralela supera a sequencial em termos de tempo de execução. No entanto, também identificamos alguns gargalos que podem ser abordados em futuras implementações.



