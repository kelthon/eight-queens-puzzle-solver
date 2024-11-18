from constants import CHESSBOARD_MAX_SCORE
from solver import GeneticAlgorithmSolver
from utils import clear_log, log, print_instance
# teste para as populações de tamanho diferentes
if __name__ == '__main__':
  run_tests = [
    {'attempts': 10, 'population_size': 150, 'max_iterations': 100, 'mutatio_prob_rate': 0.2},
    {'attempts': 10, 'population_size': 100, 'max_iterations': 100, 'mutatio_prob_rate': 0.2},
    {'attempts': 10, 'population_size': 200, 'max_iterations': 100, 'mutatio_prob_rate': 0.2},
    {'attempts': 5, 'population_size': 10, 'max_iterations': 100, 'mutatio_prob_rate': 0.2},
  ]
  results = [[0 for _ in range(test['attempts'])] for test in run_tests]

  clear_log()
  
  for i, test in enumerate(run_tests):
    for j in range(test['attempts']):
      ga = GeneticAlgorithmSolver(test['population_size'], test['max_iterations'], test['mutatio_prob_rate'])

      log(f"solver {run_tests.index(test) + 1} ({j+1}/{test['attempts']}):\n")
      instance = ga.fit()
      results[i][j] = instance.score
      log('\n')

      print('')
      print_instance(f'test {run_tests.index(test) + 1} ({j+1}/{test['attempts']})', instance)

  print('')
  for i, result in enumerate(results):
    right = 0
    wrong = 0

    for parcial_result in result:
      if parcial_result == CHESSBOARD_MAX_SCORE:
        right += 1
      else:
        wrong += 1

    print(f'Test {i+1} found the solution {right} times and did not find {wrong} out of {right+wrong} attempts')
  print("\nA log file named 'log.txt' was created. Please refer to it for more information.")
  
