# Notes

# Weighted Graphs
A weighted graph is a group of nodes where each edge (line connecting each node) has a non-negative value (most of the time > 0). The edge is usually refered to as the cost to travel between the nodes. We want to find the path of edges that will give us the lowest cost. A quick Google search shows that Dijkstra's Algorithm is the best way to do it.

# Weighted Graph, Python 3
  - Graph is a dictionary holding Nodes
  - Graph keys are the locations of each node (1-233)
  - Graph values are the Node objects
  - Node object: neighbors list contains corresponding ints that map to dictionary keys

# Neighbors Cheatsheet
  - Hard code the corners: 1, 8, 226, 233
  - Hard code the left side and right side nodes: 4 neighbors
  - Hard code top most: 3 neighbors
  - Hard code second top most, 9-15 and 219-225: 5 neighbors
  - Rest can be found with math: 6 neighbors-> (i-15), (i-8), (i-7), (i+7), (i+8), (i+15)

