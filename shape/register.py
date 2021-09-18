
from typing import Protocol
import importlib

from .shape import Shape


plugin_register = {}


class PluginInterface(Protocol):
  """Represents the interface for a plugin containing an initialise function"""

  def initilise() -> None:
    """Initialise the plugin"""

def load_module(path: str) -> PluginInterface:
  """Loads plugin module from path if matched to PluginInterface"""
  module = importlib.import_module(path)
  return module

def register_plugin(name: str, plugin: PluginInterface) -> None:
  """Register a plugin."""
  plugin_register[name] = plugin

def unregister_plugin(name: str) -> None:
  """Unregister a plugin"""
  plugin_register.pop(name)

def create(type: str, args: dict[str, any]) -> Shape:
  """Create a shape of a specific type given its name"""
  try:
    return plugin_register[type](**args)
  except KeyError:
    raise ValueError(f"unknown shape type {type}") 
  