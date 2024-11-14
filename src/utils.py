from random import randint, choices
from typing import List, Tuple
from constants import CHESSBOARD_FISRT_POSITION, CHESSBOARD_LAST_POSITION, CHESSBOARD_LOG_FILE, CHESSBOARD_MAX_SCORE
from datatypes import GAInstance, Gene
import math

def sort_by_score(instance: GAInstance):
    return instance.score


def create_random_genes() -> Gene:
    return [randint(0, 7) for i in range(8)]


def get_mutation_tax(population: List[GAInstance]) -> List[int]:
    tax = []
    total_score = 0
    
    for instance in population:
        total_score += instance.score
    
    for instance in population:
        choice_probability = instance.score / total_score
        tax.append(choice_probability)

    return tax

def get_parents(population: List[GAInstance]) -> List[Tuple[GAInstance, GAInstance]]:
    parents = []
    selected_parents = set()
    mutation_tax = get_mutation_tax(population)
        
    if len(population) % 2 != 0:
        population.append(GAInstance(1, choices(population=population, weights=mutation_tax, k=1)[0].gene))

    while len(parents) < len(population):
        couple = choices(population=population, weights=mutation_tax, k=2)
        
        while couple[0] in selected_parents or couple[1] in selected_parents:
            couple = choices(population=population, weights=mutation_tax, k=2)
                
        parents.append((couple[0], couple[1]))
        parents.append((couple[1], couple[0]))
        selected_parents.add(couple[0])
        selected_parents.add(couple[1])

    return parents


def create_instance_from_parents(parents: Tuple[GAInstance, GAInstance], gen: int) -> GAInstance:
    split_index = randint(0, 7)
    father, mother = parents
    child_gene = father.gene[:split_index] + mother.gene[split_index:]
    child = GAInstance(gen, child_gene)
    return child

def check_diagonal(instance: GAInstance, row: int, col: int, direction: int):
    collisions = 0
    col_counter = col
    row_counter = row
    incrementCol = 1
    incrementRow = 1 * direction
    valid_positions = range(CHESSBOARD_FISRT_POSITION, CHESSBOARD_LAST_POSITION)
  
    while (row_counter in valid_positions and col_counter in valid_positions):
        col_counter += incrementCol
        row_counter += incrementRow

        if 0 <= col_counter < len(instance.gene) and instance.gene[col_counter] == row_counter:
            collisions += 1
    
    return comb(2, collisions)


def fact(number: int) -> int:
    result = 1

    if number <= 0:
        return 0
    
    for i in range(number, 1, -1):
        result *= i
    
    return result


def comb(number, choices) -> float:
    if number == 0 or choices == 0:
        return 0
    elif number == choices:
        return 1
    else:
        try:
            return fact(choices) / (fact(number) * fact(choices - number))
        except:
            return 0

def score_percent(score: int) -> int:
    return math.floor(100 * score / CHESSBOARD_MAX_SCORE)

def clear_log():
    with open(CHESSBOARD_LOG_FILE, 'w') as log:
        log.close()

def log(title: str, instances: List[GAInstance] | GAInstance | None = None):
    with open(CHESSBOARD_LOG_FILE, 'a+') as logger:
        log_instance = lambda instance: logger.write(f'\t\t\tid: {i.id: 3}, {i.gen: 3} gen, score: {i.score: 2.2f}, gene: {i.gene}\n')

        logger.write(title)

        if instances is not None:
            if isinstance(instances, List):
                for i in instances:
                    log_instance(i)
            else:
                log_instance(instances)
        logger.close()

def print_instance(title: str, instance: Gene):
  table = [
    ['0 |', '.', '.', '.', '.', '.', '.', '.', '.', f'\t {title}'],
    ['1 |', '.', '.', '.', '.', '.', '.', '.', '.', f'\t id: {instance.id}'],
    ['2 |', '.', '.', '.', '.', '.', '.', '.', '.', f'\t gen: {instance.gen}'],
    ['3 |', '.', '.', '.', '.', '.', '.', '.', '.', f'\t score: {instance.score} ({score_percent(instance.score)}%)'],
    ['4 |', '.', '.', '.', '.', '.', '.', '.', '.', f'\t gene: {instance.gene}'],
    ['5 |', '.', '.', '.', '.', '.', '.', '.', '.', ''],
    ['6 |', '.', '.', '.', '.', '.', '.', '.', '.', ''],
    ['7 |', '.', '.', '.', '.', '.', '.', '.', '.', '\t see log.txt for more info'],
    ['  |', '-', '-', '-', '-', '-', '-', '-', '-', ''],
    ['   ', '0', '1', '2', '3', '4', '5', '6', '7', ''],
  ]

  for i in range(len(instance.gene)):
    j = instance.gene[i]
    table[j][i + (1 if i != 8 else 0)] = 'Q'
  
  for row in table:
    for col in row:
      end_line = '--' if table.index(row) == 8 else '  '
      print(f'{col}', end=end_line)
    print('')
