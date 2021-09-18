
from dataclasses import dataclass

@dataclass
class Triangle(object):
  height: int = 0 
  width: int = 0

  def print_area(self) -> None:
    print(f'triangle area is: {self.height * self.width / 2}')

def initilise() -> Triangle:
  return Triangle