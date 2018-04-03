import time

def read_text_build_graph(filename):
  temp_graph = {}
  file = open(filename, "r")
  for line in file:
    test = line.split(" ")
    location = int(test[0])
    cost = int(test[1])
    temp_graph[location] = cost
  return temp_graph

def add_neighbors(nodes):
  graph = {}
  for node in nodes:
    if node == 1:
      graph[node] = {node + 15: nodes[node+15], node + 8: nodes[node+8]}
    elif node == 8:
      graph[node] = {node + 7: nodes[node+7], node + 15: nodes[node+15]}
    elif node == 2 or node == 3 or node == 4 or node == 5 or node == 6 or node == 7:
      graph[node] = {node + 7: nodes[node+7], node + 15: nodes[node+15], node + 8: nodes[node+8]}
    elif node == 9 or node == 10 or node == 11 or node == 12 or node == 13 or node == 14 or node == 15:
      graph[node] = {node - 8: nodes[node-8], node + 7: nodes[node+7], node + 15: nodes[node+15], node + 8: nodes[node+8], node - 7: nodes[node-7]}
    elif node == 226:
      graph[node] = {node - 15: nodes[node-15], node - 7: nodes[node-7]}
    elif node == 233:
      graph[node] = {node - 8: nodes[node-8], node - 15: nodes[node-15]}
    elif node == 227 or node == 228 or node == 229 or node == 230 or node == 231 or node == 232:
      graph[node] = {node - 8: nodes[node-8], node - 15: nodes[node-15], node - 7: nodes[node-7]}
    elif node == 219 or node == 220 or node == 221 or node == 222 or node == 223 or node == 224 or node == 225:
      graph[node] = {node + 7: nodes[node+7], node - 8: nodes[node-8], node - 15: nodes[node-15], node - 7: nodes[node-7], node + 8: nodes[node+8]}
    elif node == 16 or node == 31 or node == 46 or node == 61 or node == 76 or node == 91 or node == 106 or node == 121 or node == 136 or node == 151 or node == 166 or node == 181 or node == 196 or node == 211:
      graph[node] = {node - 15: nodes[node-15], node - 7: nodes[node-7], node + 8: nodes[node+8], node + 15: nodes[node+15]}
    elif node == 23 or node == 38 or node == 53 or node == 68 or node == 83 or node == 98 or node == 113 or node == 128 or node == 143 or node == 158 or node == 173 or node == 188 or node == 203 or node == 218:
      graph[node] = {node - 15: nodes[node-15], node - 8: nodes[node-8], node + 7: nodes[node+7], node + 15: nodes[node+15]}
    else:
      graph[node] = {node - 15: nodes[node-15], node - 8: nodes[node-8], node - 7: nodes[node-7], node + 15: nodes[node+15], node + 8: nodes[node+8], node - 7: nodes[node-7]}
  return graph

def find_shortest_path(graph, start, end):
  shortest_distance = {}
  previous = {}
  unvisted = graph
  path = []
  for k in graph:
    shortest_distance[k] = 999
  shortest_distance[start] = 0
  while unvisted:
    minimumNode = None
    for node in unvisted:
      if minimumNode == None:
        minimumNode = node
      elif shortest_distance[node] < shortest_distance[minimumNode]:
        minimumNode = node
    for k, v in graph[minimumNode].items():
      if v+shortest_distance[minimumNode] < shortest_distance[k]:
        shortest_distance[k] = v + shortest_distance[minimumNode]
        previous[k] = minimumNode
    del unvisted[minimumNode]
  currentNode = end
  while currentNode != start:
    path.append(currentNode)
    currentNode = previous[currentNode]
  print(path)

def main():
  start_time = time.time()
  nodes = read_text_build_graph("test1.txt")
  graph = add_neighbors(nodes)
  find_shortest_path(graph, 226, 8)
  print("Run Time: ----%s seconds----" %(time.time() - start_time))

if __name__ == '__main__':
  main()
