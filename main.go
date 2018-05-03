package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

// Switch to removing negative ones... keep playing with this
func getNeighbors(graph map[int]map[int]int, nodes map[int]int) {
	for k := range nodes {
		if k == 1 {
			graph[k] = map[int]int{k + 15: nodes[k+15], k + 8: nodes[k+8]}
		} else if k == 8 {
			graph[k] = map[int]int{k + 7: nodes[k+7], k + 15: nodes[k+15]}
		} else if k == 2 || k == 3 || k == 4 || k == 5 || k == 6 || k == 7 {
			graph[k] = map[int]int{k + 7: nodes[k+7], k + 15: nodes[k+15], k + 8: nodes[k+8]}
		} else if k == 9 || k == 10 || k == 11 || k == 12 || k == 13 || k == 14 || k == 15 {
			graph[k] = map[int]int{k - 8: nodes[k-8], k + 7: nodes[k+7], k + 15: nodes[k+15], k + 8: nodes[k+8], k - 7: nodes[k-7]}
		} else if k == 226 {
			graph[k] = map[int]int{k - 15: nodes[k-15], k - 7: nodes[k-7]}
		} else if k == 233 {
			graph[k] = map[int]int{k - 8: nodes[k-8], k - 15: nodes[k-15]}
		} else if k == 227 || k == 228 || k == 229 || k == 230 || k == 231 || k == 232 {
			graph[k] = map[int]int{k - 8: nodes[k-8], k - 15: nodes[k-15], k - 7: nodes[k-7]}
		} else if k == 219 || k == 220 || k == 221 || k == 222 || k == 223 || k == 224 || k == 225 {
			graph[k] = map[int]int{k + 7: nodes[k+7], k - 8: nodes[k-8], k - 15: nodes[k-15], k - 7: nodes[k-7], k + 8: nodes[k+8]}
		} else if k == 16 || k == 31 || k == 46 || k == 61 || k == 76 || k == 91 || k == 106 || k == 121 || k == 136 || k == 151 || k == 166 || k == 181 || k == 196 || k == 211 {
			graph[k] = map[int]int{k - 15: nodes[k-15], k - 7: nodes[k-7], k + 8: nodes[k+8], k + 15: nodes[k+15]}
		} else if k == 23 || k == 38 || k == 53 || k == 68 || k == 83 || k == 98 || k == 113 || k == 128 || k == 143 || k == 158 || k == 173 || k == 188 || k == 203 || k == 218 {
			graph[k] = map[int]int{k - 15: nodes[k-15], k - 8: nodes[k-8], k + 7: nodes[k+7], k + 15: nodes[k+15]}
		} else {
			graph[k] = map[int]int{k - 15: nodes[k-15], k - 8: nodes[k-8], k - 7: nodes[k-7], k + 15: nodes[k+15], k + 8: nodes[k+8], k - 7: nodes[k-7]}
		}
	}
}

func findLowestCostPath(graph map[int]map[int]int, startNode int, endNode int, nodes map[int]int) {
	// holds shortest distances of all the nodes
	shortestDistance := make(map[int]int)
	// map of previous nodes
	previous := make(map[int]int)
	// holds the unvisited nodes
	unvisited := make(map[int]map[int]int)
	// All Maps in Go are references in memory
	// so we copy graph over so we don't overwrite
	for k, v := range graph {
		unvisited[k] = v
	}
	// Our final answer list
	path := make([]int, 0)
	// First set each node to a large number
	for k := range graph {
		shortestDistance[k] = 999
	}
	// Set first node cost to 0
	shortestDistance[startNode] = 0
	// while there are still unvisited nodes
	// loop
	for len(unvisited) > 0 {
		var minimumNode int
		i := 0
		// Find the next low cost node in the map
		// of unvisited tiles
		for k := range unvisited {
			if i == 0 {
				minimumNode = k
				i = i + 1
				// If the distance at k is less than the shortest distance at the
				// minimum node then update the minimum node
			} else if shortestDistance[k] < shortestDistance[minimumNode] {
				minimumNode = k
			}
		}
		// Loop through the neighbors at the minimum node
		for k, v := range graph[minimumNode] {
			/*
				If the cost of the neighbor + the cost of the
				shortest distance at the minimum node is less than the cost at the
				shortest distance at k then we've found the next tile in our path.
				Update previous map and the shortest distance at k
				v + shortestDistance[minimumNode] is equal to the cost of the neighbors
				plus the current tile we are on. shortestDistance[k] is equal to the cost
				of the current neighbor.
			*/
			if v+shortestDistance[minimumNode] < shortestDistance[k] {
				shortestDistance[k] = v + shortestDistance[minimumNode]
				previous[k] = minimumNode
			}
		}
		// Delete the minimum node index from map of
		// unvisited tiles
		delete(unvisited, minimumNode)
	}
	// Once we have set everything up we can now
	// get the current path

	// Start at the ending node (8)
	currentNode := endNode
	// while the currentNode doesn't equal the start node (233? I forget)
	for currentNode != startNode {
		// Add the current node to the path list
		path = append(path, currentNode)
		// Set the current node to the previous node
		currentNode = previous[currentNode]
	}
	// create our path answer
	// add start node
	path = append(path, startNode)
	// Reverse the path list cause it's initially backwards
	for index := len(path)/2 - 1; index >= 0; index-- {
		opp := len(path) - 1 - index
		path[index], path[opp] = path[opp], path[index]
	}
	// fmt.Printf("%v\n", path)
	// fmt.Printf("Lowest Cost: [%d]\n", shortestDistance[endNode]+nodes[startNode])
	// for _, node := range path {
	// 	fmt.Println(node)
	// 	fmt.Println()
	// }
	// fmt.Printf("Minimal Path Cost = %d\n", shortestDistance[endNode]+nodes[startNode])
	// fmt.Println()
	outputFile, _ := os.Create("test_output_2.txt")
	defer outputFile.Close()
	for _, node := range path {
		fmt.Fprintf(outputFile, "%d\n", node)
	}
	fmt.Fprintf(outputFile, "Minimal Path Costs: %d\n", shortestDistance[endNode]+nodes[startNode])
}

// Remove all the negative ones from the graph
func removeNegativeOnes(graph map[int]map[int]int) {
	for _, v := range graph {
		for node, cost := range v {
			if cost == -1 {
				delete(v, node)
			}
		}
	}
}

func main() {
	// Start timer to measure performance
	start := time.Now()
	// Initialize vars
	graph := make(map[int]map[int]int)
	nodes := make(map[int]int)
	//file, fileError := os.Open("test_input_2.txt")
	file, fileError := os.Open(os.Args[1])
	if fileError != nil {
		fmt.Println(fileError)
	}
	reader := bufio.NewScanner(file)
	// Load all of the points in
	for reader.Scan() {
		line := reader.Text()
		nums := strings.Split(line, " ")
		// Added because it seems all of Root's text files
		// end with two empty lines so we need to stop once we
		// hit an empty line (it seems empty arrays in Go still have a length of 1 lol)
		if len(nums) == 1 {
			break
		}
		// Convert lines to ints and add them to the graph
		location, _ := strconv.Atoi(nums[0])
		cost, _ := strconv.Atoi(nums[1])
		nodes[location] = cost
	}
	getNeighbors(graph, nodes)
	removeNegativeOnes(graph)
	findLowestCostPath(graph, 226, 8, nodes)
	end := time.Since(start)
	fmt.Printf("Shortest Path Found In: [%s]\n", end)
}
