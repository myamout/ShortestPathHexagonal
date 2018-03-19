from Node import Node

graph = {}

def read_text_build_graph(filename):
  temp_graph = {}
  file = open(filename, "r")
  for line in file:
    test = line.split(" ")
    location = int(test[0])
    cost = int(test[1])
    temp_graph[location] = Node(location, cost)
  return temp_graph

def main():
  graph = read_text_build_graph("test1.txt")
  for k, v in graph.items():
    print(v.to_string())

if __name__ == '__main__':
  main()
