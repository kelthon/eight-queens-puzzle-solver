from random import randint, choices
from typing import List, Tuple
from constants import CHESSBOARD_FISRT_POSITION, CHESSBOARD_LAST_POSITION, CHESSBOARD_SCORE_MODIFIER
from datatypes import GAInstance, Gene

def sort_by_score(a: GAInstance, b: GAInstance):
    return a.score - b.score


def create_random_genes() -> Gene:
    return [randint(0, 7) for i in range(8)]


def extract_scores_from_list(population: List[GAInstance]) -> List[int]:
    scores = []
    population_len = len(population)

    for instance in population:
        choice_probability = instance.score / population_len
        scores.append(choice_probability)

    return scores


def get_parents(population: List[GAInstance]) -> List[Tuple[GAInstance, GAInstance]]:
    parents = []
    select_list = population[:]
    scores = extract_scores_from_list(population)
        
    while len(select_list) > 0:
        couple = choices(population=select_list, weights=scores, k=2)
        parents.append((couple[0], couple[1]))
        parents.append((couple[1], couple[0]))
        select_list.remove(couple[0], couple[1])

    return parents


def create_instance_from_parents(parents: Tuple[GAInstance, GAInstance], gen: int) -> GAInstance:
    split_index = randint(0, 7)
    father, mother = parents
    child = GAInstance(gen, father[:split_index] + mother[split_index + 1 : ])
    return child

def check_diagonal(row: int, col: int, direction: int):
    score = 0
    col_counter = col
    row_counter = row
    increment = direction
    valid_positions = range(CHESSBOARD_FISRT_POSITION, CHESSBOARD_LAST_POSITION)
                    
    while (row_counter in valid_positions and col_counter in valid_positions):
        col_counter += increment
        row_counter += increment

        if instance.gene[col_counter] == row_counter:
            score -= CHESSBOARD_SCORE_MODIFIER
    
    return score
