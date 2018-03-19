'''
Neighbors Array: Key values for Graph dictionary
'''

class Node:
  def __init__(self, location, cost):
    self.location = location
    self.cost = cost
    self.neighbors = []
    self.visited = False
  
  def set_visited(self):
    self.visited = True
  
  def get_location(self):
    return self.location
  
  def get_cost(self):
    return cost
  
  def to_string(self):
    return "Location: ["+str(self.location)+"], Cost: ["+str(self.cost)+"]"
  
  '''
  def add_neighbor(self...)
  def get_neighbors(self)
  To be implemented
  '''