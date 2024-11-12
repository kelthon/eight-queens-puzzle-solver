from solver import GeneticAlgorithmSolver
from datatypes import Gene
from utils import clear_log, log

def print_instance(instance: Gene):
  table = [
    ['0 |', '.', '.', '.', '.',  '.', '.', '.', '.', f'\t id: {instance.id}'],
    ['1 |', '.', '.', '.', '.',  '.', '.', '.', '.', f'\t gen: {instance.gen}'],
    ['2 |', '.', '.', '.', '.',  '.', '.', '.', '.', f'\t score: {instance.score}'],
    ['3 |', '.', '.', '.', '.',  '.', '.', '.', '.', f'\t gene: {instance.gene}'],
    ['4 |', '.', '.', '.', '.',  '.', '.', '.', '.', ''],
    ['5 |', '.', '.', '.', '.',  '.', '.', '.', '.', ''],
    ['6 |', '.', '.', '.', '.',  '.', '.', '.', '.', ''],
    ['7 |', '.', '.', '.', '.',  '.', '.', '.', '.', ''],
    ['  |', '-', '-', '-', '-',  '-', '-', '-', '-', ''],
    ['  ', '0', '1', '2', '3', '4', '5', '6', '7'],
  ]

  for i in range(len(instance.gene)):
    j = instance.gene[i]
    table[j][i + (1 if i == 0 else 0)] = 'Q'
  
  for row in table:
    for col in row:
      end_line = '--' if table.index(row) == 8 else '  '
      print(f'{col}', end=end_line)
    print('')


if __name__ == '__main__':
  run_tests = [
    {'population_size': 10, 'max_iterations': 100, 'mutatio_prob_rate': 0.2},
    {'population_size': 20, 'max_iterations': 100, 'mutatio_prob_rate': 0.2},
    {'population_size': 40, 'max_iterations': 100, 'mutatio_prob_rate': 0.3},
  ]

  clear_log()

  for param in run_tests:
    solver = GeneticAlgorithmSolver(param['population_size'], param['max_iterations'], param['mutatio_prob_rate'])

    log(f"solver {run_tests.index(param) + 1}:\n")
  
    instance = solver.fit()
  
    log('\n')

    print(f'\nsolver {run_tests.index(param) + 1}')
    print_instance(instance)

