import time
from Node import Node

def read_text_build_graph(filename):
  temp_graph = {}
  file = open(filename, "r")
  for line in file:
    test = line.split(" ")
    location = int(test[0])
    cost = int(test[1])
    temp_graph[location] = Node(location, cost)
  return temp_graph

def add_neighbors(graph):
  for k, v in graph.items():
    # Top two corners
    if k == 1 or k == 8:
      neighbors = [k+8, k+15]
      graph[k].add_neighbors(neighbors, graph)
    # Bottom two corners
    elif k == 226 or k == 233:
      neighbors = [k-7, k-15]
      graph[k].add_neighbors(neighbors, graph)
    # Top middle
    elif k == 2 or k == 3 or k == 4 or k == 5 or k == 6 or k == 7:
      neighbors = [k+7, k+15, k+8]
      graph[k].add_neighbors(neighbors, graph)
    # Top second row down
    elif k == 9 or k == 10 or k == 11 or k == 12 or k == 13 or k == 14 or k == 15:
      neighbors = [k-8, k+7, k+15, k+8, k-7]
      graph[k].add_neighbors(neighbors, graph)
    # Bottom middle
    elif k == 227 or k == 228 or k == 229 or k == 230 or k == 231 or k == 232:
      neighbors = [k-8, k-15, k-7]
      graph[k].add_neighbors(neighbors, graph)
    # Bottom Second Row
    elif k == 219 or k == 220 or k == 221 or k == 222 or k == 223 or k == 224 or k == 225:
      neighbors = [k+7, k-8, k-15, k-7, k+8]
      graph[k].add_neighbors(neighbors, graph)
    # Left side column
    elif k == 16 or k == 31 or k == 46 or k == 61 or k == 76 or k == 91 or k == 106 or k == 121 or k == 136 or k == 151 or k == 166 or k == 181 or k == 196 or k == 211:
      neighbors = [k-15, k-7, k+8, k+15]
      graph[k].add_neighbors(neighbors, graph)
    # Right side column
    elif k == 23 or k == 38 or k == 53 or k == 68 or k == 83 or k == 98 or k == 113 or k == 128 or k == 143 or k == 158 or k == 173 or k == 188 or k == 203 or k == 218:
      neighbors = [k-15, k-8, k+7, k+15]
      graph[k].add_neighbors(neighbors, graph)
    # Rest of the tiles
    else:
      neighbors = [k-15, k-8, k+7, k+15, k+8, k-7]
      graph[k].add_neighbors(neighbors, graph)

def grab_costs_of_neighbors(neighbors):
  temp = neighbors.values()
  costs = []
  for node in temp:
    costs.append(node.get_cost())
  return costs

def find_shortest_path(visited, unvisited, min_cost, path, graph):
  bool path_found = False
  # Add starting point, vist it, grab neighbors
  path.append(graph[226])
  neighbors = graph[226].get_neighbors()
  visited.append(graph[226].get_location())
  unvisited.remove(226)
  while path_found:
    costs = grab_costs_of_neighbors(neighbors)
    updated_costs = [x + min_cost for x in costs]
    lowest_cost = min(updated_costs)

def main():
  start_time = time.time()
  graph = read_text_build_graph("test1.txt")
  add_neighbors(graph)
  visited = []
  unvisited = graph.keys()
  min_cost = 0
  path = []
  find_shortest_path(visited, unvisited, min_cost, path, graph)
  print("Run Time: ----%s seconds----" %(time.time() - start_time))

if __name__ == '__main__':
  main()
