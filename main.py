"""
Basic exmaple showing how to create objects from data using a dynamic factory
with plugins
"""

import json
from math import pi
from dataclasses import dataclass

from shape import register
from shape.shape import Circle, Square


def main() -> None:

  # read data from json file
  with open("./data.json") as file:
    data = json.load(file)

  # register native plugins
  register.register_plugin("circle", plugin=Circle)
  register.register_plugin("square", plugin=Square)

  # import the plugins
  for plugin in data["plugins"]:
    module = register.load_module(plugin["path"]).initilise()
    register.register_plugin(plugin["name"], plugin=module)

  # create the shapes 
  shapes = []
  for shape in data["shapes"]:
    shape_copy = shape.copy()
    type = shape_copy.pop("type") 
    shapes.append(register.create(type, shape_copy)) 

  # call area on shapes
  for shape in shapes:
    shape.print_area()

if __name__ == "__main__":
  main() 