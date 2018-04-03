"""
CS560 Algorithms
David Arce & Matt Yamout (Python Version)
Group Assignment
"""

import time

def read_text_build_graph(filename):
    temp_graph = {}
    file = open(filename, "r")
    for line in file:
        test = line.split(" ")
        location = int(test[0])
        cost = int(test[1])
        temp_graph[location] = {'cost':cost}
        # Node(location, cost)
    return temp_graph


def add_neighbors(graph):
    for k in graph.keys():
        # Top two corners
        if k == 1 or k == 8:
            if k == 1:
                neighbors = [k+8, k+15]
                graph[k].update({'nei_loc': neighbors})
            elif k == 8:
                neighbors = [k+7, k+15]
                graph[k].update({'nei_loc': neighbors})
        # Bottom two corners
        elif k == 226 or k == 233:
            if k == 226:
                neighbors = [k-7, k-15]
                graph[k].update({'nei_loc': neighbors})
            elif k == 233:
                neighbors = [k-8, k-15]
                graph[k].update({'nei_loc': neighbors})
        # Top middle
        elif 2 <= k <= 7:
            # bot_left, bottom, bot_right
            neighbors = [k+7, k+15, k+8]
            graph[k].update({'nei_loc': neighbors})
        # Top second row down
        elif 9 <= k <= 15:
            # top_left, bot_left, bottom, bot_right, top_right
            neighbors = [k-8, k+7, k+15, k+8, k-7]
            graph[k].update({'nei_loc': neighbors})
        # Bottom middle
        elif 227 <= k <= 232:
            # top_left, top, top_right
            neighbors = [k-8, k-15, k-7]
            graph[k].update({'nei_loc': neighbors})
        # Bottom Second Row
        elif 219 <= k <= 225:
            # bot_left, top_left, top, top_right, bot_right
            neighbors = [k+7, k-8, k-15, k-7, k+8]
            graph[k].update({'nei_loc': neighbors})
        # Left side column
        elif k == 16 or k == 31 or k == 46 or k == 61 or k == 76 or k == 91 or k == 106 or k == 121 or k == 136 or k == 151 or k == 166 or k == 181 or k == 196 or k == 211:
            # top, top_right, bot_right, bottom
            neighbors = [k-15, k-7, k+8, k+15]
            graph[k].update({'nei_loc': neighbors})
        # Right side column
        elif k == 23 or k == 38 or k == 53 or k == 68 or k == 83 or k == 98 or k == 113 or k == 128 or k == 143 or k == 158 or k == 173 or k == 188 or k == 203 or k == 218:
            # top, top_left, bot_left, bottom
            neighbors = [k-15, k-8, k+7, k+15]
            graph[k].update({'nei_loc': neighbors})
        # Rest of the tiles MIDDLE
        else:
            # top, top_left, bot_left, bottom, bot_right, top_right
            neighbors = [k-15, k-8, k+7, k+15, k+8, k-7]
            graph[k].update({'nei_loc': neighbors})

def find_shortest_path(graph, start, end):
    shortest_distance = {}
    previous = {}
    unvisited = {}
    path= []
    for k,v in graph.items():
        if v['cost'] != -1:
            unvisited[k] = True
    
    for k,v in graph.items():
        if v['cost'] != -1:
            shortest_distance[k] = 999

    shortest_distance[start] = 0

    while len(unvisited) > 0:
        minNode = None
        i = 0
        for k,v in unvisited.items():
            if i == 0:
                minNode = k
                i += 1
            elif shortest_distance[k] < shortest_distance[minNode]:
                minNode = k

        for k in graph[minNode]['nei_loc']:
            if k in unvisited:
                if (graph[k]['cost'] + shortest_distance[minNode]) < shortest_distance[k]:
                    shortest_distance[k] = graph[k]['cost'] + shortest_distance[minNode]
                    previous[k] = minNode
                    # print(k)
                    
        del unvisited[minNode]

    currentNode = end
    while currentNode != start:
        path.append(currentNode)
        currentNode = previous[currentNode]
    path.append(currentNode)
    path.reverse()
    print('Shortest Path:', path)
    print('Lowest Cost:', shortest_distance[end]+graph[start]['cost'])


def main():
    start_time = time.time()
    graph = read_text_build_graph("test1.txt")
    add_neighbors(graph)
    find_shortest_path(graph, 226, 8)
    print("Run Time: ----%s milliseconds ----" %((time.time() - start_time)*1000))

if __name__ == '__main__':
  main()
