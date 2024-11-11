from typing import Tuple
from dataclasses import dataclass

type Gene = Tuple[int, int, int, int, int, int, int, int]

@dataclass
class GAInstance:
  __instance_counter = 0
  
  def __init__(self, gen: int, gene: Gene):
    self.__instance_counter += 1
    self.__id = self.__instance_counter
    self.__gen = gen
    self.__gene = gene
  
  @property
  def id(self) -> int:
    return self.__id
  
  @property
  def gen(self) -> int:
    return self.__gen
  
  @property
  def gene(self) -> Gene:
    return self.__gene
  
  