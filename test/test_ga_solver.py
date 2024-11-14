import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from solver import GeneticAlgorithmSolver

def test_solver():
  ga = GeneticAlgorithmSolver(0, 0, 0)
  assert isinstance(ga, GeneticAlgorithmSolver)