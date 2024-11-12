from typing import Literal, Tuple
from itertools import count

GeneValue = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
Gene = Tuple[GeneValue, GeneValue, GeneValue, GeneValue, GeneValue, GeneValue, GeneValue, GeneValue]

class GAInstance:
  __instance_counter = count(0)
  
  def __init__(self, gen: int, gene: Gene):
    self.__id = next(self.__instance_counter)
    self.__gen = gen
    self.__gene = gene
    self.score = 0
  
  @property
  def id(self) -> int:
    return self.__id
  
  @property
  def gen(self) -> int:
    return self.__gen
  
  @property
  def gene(self) -> Gene:
    return self.__gene

  @property
  def score(self) -> int:
    return self.__score

  @score.setter
  def score(self, score_points: int) -> None:
    self.__score = score_points

  def mutate_gene(self, gene_index: int, gene_value: GeneValue) -> None:
    self.__gene[gene_index] = gene_value

  def __repr__(self):
    return f'{self.gene}'
  

  