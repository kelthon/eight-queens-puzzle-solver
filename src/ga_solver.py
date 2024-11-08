from random import randint
from typing import List
from constants import CHESSBOARD_LAST_POSITION

class GeneticAlgorithmSolver:
    _max_iterations: int
    _population_size: int
    _population: List[List[int]]
    _mutation_probability_rate: float

    def __init__(
        self,
        population_size: int,
        max_iterations: int,
        mutation_probability_rate: float
    ) -> None:
        self._max_iterations = max_iterations
        self._population_size = population_size
        self._mutation_probability_rate = mutation_probability_rate
        self._population = []
    
    @property
    def population(self):
        return self._population

    def init(self):
        '''creates a random population'''
        for i in range(self._population_size):
            instance = [randint(0, 7) for j in range(8)]
            self._population.append(instance)
    
    def evaluate(self, instance):
        '''fitness funtion to evaluate a instance'''
        pass

    def select(self):
        '''selects the best instances of population'''
        best_instances = self.population.sort()[:self._population_size]
        self._population = best_instances

        return best_instances[0]

    def crossover(self):
        '''reproduce instances using crossover to generate new instances'''
        children = []
        
        for i in range(0, self._population_size, 2):
            split_index = randint(0, CHESSBOARD_LAST_POSITION)
            parents = self.population[i], self.population[i + 1]
            child = [parents[0][:split_index] + parents[1][split_index + 1:]]
            children.append(child)

        return children

    def mutate(self, children):
        '''matates the instances to improve genetic variablility'''
        for child in children:
            for gene in child:
                if randint(1, self._mutation_probability_rate) == self._mutation_probability_rate:
                    gene = randint(0, CHESSBOARD_LAST_POSITION)

        return children


    def fit(self):
        '''starts the fitness of all instances'''
        self.init()

        for i in range(self._max_iterations):
            children = self.crossover()
            children = self.mutate(children)
            top_one = self.select()
