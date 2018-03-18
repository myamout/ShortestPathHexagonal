# Notes

# Weighted Graphs
A weighted graph is a group of nodes where each edge (line connecting each node) has a non-negative value (most of the time > 0). The edge is usually refered to as the cost to travel between the nodes. We want to find the path of edges that will give us the lowest cost. A quick Google search shows that Dijkstra's Algorithm is the best way to do it.

# Weighted Graph, Python 3
  - We'll need to implement a graph data structure
  - Our Graph data structure will hold node classes

# Algo
  1. Start at bottom left corner
  2. Compare neighbors for the cheapest cost
  3. Move to cheapest neighbor and mark all previously checked neighbors as visited
  4. Repeat until we've reached the top right corner

