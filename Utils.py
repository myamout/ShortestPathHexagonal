from Node import Node

class Utils:

  def __init__(self):
    self.graph = []

  def read_text_file(self, filename):
    file = open(filename, "r")
    for line in file:
      print(line)
  
  def add_node(self, location, cost):
    pass
