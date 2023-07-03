from sudoku_boards import *
from algorithms import *

import copy
from tabulate import tabulate
import time


def calc_t_and_steps(solver: SudokuSolver):
    start = time.time()
    solver.solve_sudoku()
    tiempo = (time.time() - start)*1000

    return tiempo, solver.steps

# Creamos objetos solver
backtracking_solver = BacktrackingSolver(copy.deepcopy(sudoku_board_dani))
forwardchecking_solver = ForwardCheckingSolver(copy.deepcopy(sudoku_board_dani))

# Calcular tiempos y pasos requeridos
t_backtracking, steps_backtracking = calc_t_and_steps(backtracking_solver)
t_forwardchecking, steps_forward = calc_t_and_steps(forwardchecking_solver)

# Inicializamos la tabla
tabla = [
    ["Backtracking", t_backtracking, steps_backtracking],
    ["Forward Checking", t_forwardchecking, steps_forward],
]

# Imprimimos tabla
headers = ["Algoritmo", "Tiempo (ms)", "Pasos"]
print(tabulate(tabla, headers=headers, tablefmt="grid"))
