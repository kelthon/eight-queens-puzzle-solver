from ga_solver import GeneticAlgorithmSolver

a = [10, 10000, 0.2]

solver = GeneticAlgorithmSolver(a[0], a[1], a[2])

solver.fit()
