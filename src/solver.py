from random import randint, random
from typing import Callable, List
from constants import CHESSBOARD_DOWN_DIAGONAL, CHESSBOARD_FISRT_POSITION, CHESSBOARD_LAST_POSITION, CHESSBOARD_LENGHT, CHESSBOARD_MAX_SCORE, CHESSBOARD_SCORE_MODIFIER, CHESSBOARD_UP_DIAGONAL
from datatypes import GAInstance
from utils import comb, create_instance_from_parents, create_random_genes, get_parents, sort_by_score, check_diagonal, log

class GeneticAlgorithmSolver:
    def __init__(
        self,
        population_size: int,
        max_iterations: int,
        mutation_probability_rate: float
    ) -> None:
        self._max_iterations = max_iterations
        self._population_size = population_size
        self._mutation_probability = mutation_probability_rate
        self._generations_counter = 1
        self._population = []

    def init(self) -> List[GAInstance]:
        '''creates a random population'''
        for i in range(self._population_size):
            gene = create_random_genes()
            instance = GAInstance(1, gene)
            self.fitness(instance)
            self._population.append(instance)

        return self._population
    
    def fitness(self, instance: GAInstance) -> int:
        '''fitness funtion to evaluate a instance'''
        score = CHESSBOARD_MAX_SCORE
        rows_set = []

        for col in range(CHESSBOARD_LENGHT):
            row = instance.gene[col]

            # Checks if two or more queens are in same row in a instance 
            if row in rows_set:
                score -= comb(2, rows_set.count(row) + 1)

            # Checks if two or more queens are in same diagonals
            else:
                if (col == CHESSBOARD_FISRT_POSITION and row == CHESSBOARD_FISRT_POSITION) or (row == CHESSBOARD_FISRT_POSITION):
                    score -= check_diagonal(instance, row, col, CHESSBOARD_DOWN_DIAGONAL)

                elif (col == CHESSBOARD_FISRT_POSITION and row == CHESSBOARD_LAST_POSITION) or (row == CHESSBOARD_LAST_POSITION):
                    score -= check_diagonal(instance, row, col, CHESSBOARD_UP_DIAGONAL)
    
                else:
                    score -= check_diagonal(instance, row, col, CHESSBOARD_UP_DIAGONAL)
                    score -= check_diagonal(instance, row, col, CHESSBOARD_DOWN_DIAGONAL)

            rows_set.append(row)
            instance.score = score
        return score

    def select(self, number_of_instances: int | None = None) -> List[GAInstance]:
        '''selects the best instances of population'''
        self._population.sort(key=sort_by_score, reverse=True)
        best_instances = self._population
        self._population = best_instances[:self._population_size]

        
        return best_instances[:number_of_instances] if isinstance(number_of_instances, int) else best_instances

    def crossover(self) -> List[GAInstance]:
        '''reproduce instances using crossover to generate new instances'''
        children = []

        if len(self._population) % 2 != 0:
            children.append(self._population.pop())

        parents = get_parents(self._population)
        
        for couple in parents:
            child = create_instance_from_parents(couple, self._generations_counter)
            children.append(child)


        return children

    def mutate(self, children: List[GAInstance]) -> List[GAInstance]:
        '''mutates children instances to improve genetic variablility'''
        for child in children:
            for i in range(len(child.gene)):
                if random() < self._mutation_probability:
                    child.mutate_gene(i, randint(CHESSBOARD_FISRT_POSITION, CHESSBOARD_LAST_POSITION))

        return children


    def fit(self) -> GAInstance:
        '''starts the fitness of all instances'''
        self.init()
        parents = self.select(self._population_size)
            
        for i in range(self._max_iterations):         
            self._generations_counter += 1
            
            children = self.crossover()
            children = self.mutate(children)
            
            for instance in children:
                self.fitness(instance)

            self._population.extend(children)

            all_instances = self.select()
            best_instances = self._population

            log(f'\titeration {i}:\n')
            log('\t\tall instances:\n', all_instances)
            log('\t\tparents:\n', parents)
            log('\t\tchildren:\n', children)
            log('\t\tbest intances:\n', best_instances)
            log('\n')
        
        return best_instances[0]
    