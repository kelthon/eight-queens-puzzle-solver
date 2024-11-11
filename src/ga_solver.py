from random import randint
from typing import List
from constants import CHESSBOARD_LAST_POSITION
from datatypes import GAInstance
from utils import create_instance_from_parents, create_random_genes, get_best_instances, get_parents, sort_by_score

class GeneticAlgorithmSolver:
    def __init__(
        self,
        population_size: int,
        max_iterations: int,
        mutation_probability_rate: float
    ) -> None:
        self._max_iterations = max_iterations
        self._population_size = population_size
        self._mutation_probability_rate = mutation_probability_rate
        self._generations_counter = 0
        self._population = []

    def init(self) -> List[GAInstance]:
        '''creates a random population'''
        for i in range(self._population_size):
            gene = create_random_genes()
            instance = GAInstance(i, gene)
            self._population.append(instance)

        return self._population
    
    def fitness(self, instance: GAInstance) -> int:
        '''fitness funtion to evaluate a instance'''
        pass

    def select(self, number_of_instances: int = 5) -> GAInstance:
        '''selects the best instances of population'''
        self._population.sort(key=sort_by_score)
        best_instances = self._population[:self._population_size]
        self._population = best_instances

        return best_instances[:number_of_instances]

    def crossover(self) -> List[GAInstance]:
        '''reproduce instances using crossover to generate new instances'''
        children = []
        
        parents = get_parents(self._population)
        
        for parent in parents:
            child = create_instance_from_parents(parent, self._generations_counter)
            children.append(child)

        return children

    def mutate(self, children: List[GAInstance]) -> List[GAInstance]:
        '''mutates children instances to improve genetic variablility'''
        for child in children:
            for gene in child:
                if randint(1, self._mutation_probability_rate) == self._mutation_probability_rate:
                    child[child.index(gene)] = randint(0, CHESSBOARD_LAST_POSITION)

        return children


    def fit(self):
        '''starts the fitness of all instances'''
        self.init()

        for i in range(self._max_iterations):
            self._generations_counter += 1
            children = self.crossover()
            children = self.mutate(children)
            top_one = self.select()
            print(f'{i}° gen: {top_one}')
