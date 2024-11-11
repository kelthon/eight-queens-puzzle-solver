from random import randint
from typing import List, Tuple
from constants import CHESSBOARD_LENGHT, CHESSBOARD_MAX_SCORE, CHESSBOARD_SCORE_MODIFIER
from datatypes import GAInstance, Gene

def sort_by_score(a: GAInstance, b: GAInstance):
    return a.score - b.score


def create_random_genes() -> Gene:
    return [randint(0, 7) for i in range(8)]


def get_parents(population: List[GAInstance]) -> List[Tuple[GAInstance, GAInstance]]:
    parents = []
    couple = []
    reverse_couple = []

    for instance in population:
        pass
    
    return parents


def create_instance_from_parents(parents: Tuple[GAInstance, GAInstance], gen: int) -> GAInstance:
    split_index = randint(0, 7)
    father, mother = parents
    child = father[:split_index] + mother[split_index + 1 : ]

    return child


def evaluate(instance) -> int:
    score = CHESSBOARD_MAX_SCORE
    rows_set = []
    cols_set = []

    for col in range(CHESSBOARD_LENGHT):
        row = instance[col]

        # Checks if two or more queens are in same row in a instance 
        if row in rows_set:
            score -= CHESSBOARD_SCORE_MODIFIER

        # Checks if two or more queens are in same diagonals
        else:
        #
        # checking diagonals we have four possibilties:
        #   1. queen is int the coners and has one diagonal
        #   2. queen is in the edges and has two diagonals
        #   3. queen is in the middle and has four diagonals
        #   
        #   0 . . . 1 . 2 .
        #   . 0 . 1 . 2 . 2
        #   1 . 0 . 2 . . .
        #   . 1 . 0 . . . .
        #   1 . 1 . 0 . . .
        #   . 2 . 1 . 0 . .
        #   2 . . . 1 . 0 .
        #   . . . . . 1 . 0
            if col == 0:
                col_counter, row_counter = col, row
                    
                while row_counter < CHESSBOARD_LENGHT or col_counter < CHESSBOARD_LENGHT:
                    col_counter += 1
                    row_counter += 1

                    if instance[col_counter] == row_counter:
                        score -= CHESSBOARD_SCORE_MODIFIER
                
                if row != 0 and row != 7:
                    col_counter, row_counter = col, row
                    
                while row_counter >= 0 or col_counter >= 0:
                    col_counter -= 1
                    row_counter -= 1

                    if instance[col_counter] == row_counter:
                        score -= CHESSBOARD_SCORE_MODIFIER

            elif col == 7:
                if row == 0:
                    pass
                elif row == 7:
                    pass
                else:
                    pass

            else:
                if row == 0:
                    pass
                elif row == 7:
                    pass
                else:
                    pass

        rows_set.append(row)
    return score


instance = [i for i in range(CHESSBOARD_LENGHT)]
 
print(instance, evaluate(instance))
