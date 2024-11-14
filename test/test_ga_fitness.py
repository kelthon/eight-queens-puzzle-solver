import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest

from datatypes import GAInstance
from solver import GeneticAlgorithmSolver  

def test_fitness():
  param = {'attempts': 10, 'population_size': 150, 'max_iterations': 100, 'mutatio_prob_rate': 0.2}

  ga = GeneticAlgorithmSolver(param['population_size'], param['max_iterations'], param['mutatio_prob_rate'])

  assert ga.fitness(GAInstance(0, [7, 6, 3, 0, 4, 1, 5, 2])) == 27

  assert ga.fitness(GAInstance(0, [2, 0, 6, 1, 7, 5, 3, 0])) == 27
  
  assert ga.fitness(GAInstance(0, [2, 0, 6, 1, 7, 5, 1, 0])) == 25

  assert ga.fitness(GAInstance(0, [3, 6, 2, 7, 1, 4, 0, 5])) == 28