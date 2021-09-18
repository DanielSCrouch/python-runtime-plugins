"""Represents a shape."""

from typing import Protocol
from dataclasses import dataclass
from math import pi

class Shape(Protocol):
  """Basic representation of a shape."""


  def print_area(self) -> None:
    """Print the area of the shape."""


# Example shapes

@dataclass
class Square(object):
  length: int = 0 
  width: int = 0

  def print_area(self) -> None:
    print(f'length: {self.length}')
    print(f'width: {self.width}')
    print(f'square area is: {self.length * self.width}')

@dataclass
class Circle(object):
  radius: int = 0

  def print_area(self) -> None:
    print(f'circle area is: {2 * pi * self.radius}')
