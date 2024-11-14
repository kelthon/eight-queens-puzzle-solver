from solver import GeneticAlgorithmSolver
from datatypes import GAInstance, Gene
from utils import clear_log, log, print_instance

if __name__ == '__main__':
  run_tests = [
    {'attempts': 1, 'population_size': 10, 'max_iterations': 100, 'mutatio_prob_rate': 0.2},
    # {'attempts': 10, 'population_size': 100, 'max_iterations': 100, 'mutatio_prob_rate': 0.2},
    # {'attempts': 10, 'population_size': 200, 'max_iterations': 100, 'mutatio_prob_rate': 0.2},
  ]
  results = [[] for _ in run_tests]

  clear_log()
  
  for test in run_tests:
    for i in range(test['attempts']):
      ga = GeneticAlgorithmSolver(test['population_size'], test['max_iterations'], test['mutatio_prob_rate'])

      log(f"solver {run_tests.index(test) + 1} ({i+1}/{test['attempts']}):\n")
      instance = ga.fit()
      log('\n')

      print('')
      print_instance(f'test {run_tests.index(test) + 1} ({i+1}/{test['attempts']})', instance)

