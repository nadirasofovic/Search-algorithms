# Search Algorithms

This repository contains implementations of several search algorithms used in graph traversal and pathfinding. Specifically, it includes the following algorithms:

- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **A* Search** (with both Manhattan and Euclidean heuristics)

These algorithms are commonly used in a variety of applications, including puzzle-solving, pathfinding in games, network routing, and more.

## Algorithms Overview

### Depth-First Search (DFS)

DFS is a graph traversal algorithm that explores as deeply as possible along each branch before backtracking. It uses a stack (either explicitly or through recursion) to keep track of the nodes being explored. The algorithm starts at the initial node (S), pushes it onto the stack, and proceeds as follows:
1. Pop the top node from the stack.
2. Mark it as visited.
3. Add its unvisited neighbors to the stack.
4. Repeat the process until the goal node (G) is found or the stack is empty.

#### Key Characteristics:
- Prioritizes depth over breadth.
- Does not guarantee the shortest path in unweighted graphs.
- Requires less memory than BFS, as it stores only the current path.

#### Advantages:
- Simple and memory-efficient for exploring deep paths.
- Effective in scenarios where the entire graph needs to be explored.

#### Disadvantages:
- May explore unnecessary paths, leading to inefficiency.
- Can fail to find the shortest path.

---

### Breadth-First Search (BFS)

BFS is a graph traversal algorithm that explores all neighbors of a node before moving to the next level. It uses a queue to keep track of nodes to be explored. The algorithm starts at the initial node (S), enqueues it, and proceeds as follows:
1. Dequeue a node.
2. Mark it as visited.
3. Enqueue all its unvisited neighbors.
4. Repeat the process until the goal node (G) is found or the queue is empty.

#### Key Characteristics:
- Explores nodes level by level.
- Guarantees the shortest path in unweighted graphs.
- Requires more memory than DFS, as it stores all nodes at the current depth.

#### Advantages:
- Guarantees the shortest path is found.
- Provides a systematic exploration of all nodes.

#### Disadvantages:
- High memory usage for large graphs or dense grids.
- Slower than DFS when the goal is located deep in the graph.

---

### A* Search

A* is a pathfinding algorithm that combines the strengths of BFS and heuristics. It uses a priority queue to evaluate nodes based on the cost to reach the node and a heuristic estimate of the cost to the goal. The algorithm starts at the initial node (S), adds it to a priority queue with its cost set to 0, and proceeds as follows:
1. Remove the node with the lowest total cost (path cost + heuristic).
2. Update the costs of its neighbors and add them to the queue.
3. Repeat until the goal node (G) is reached.

#### Key Characteristics:
- Prioritizes nodes based on cost and heuristic.
- Guarantees the shortest path if the heuristic is admissible (never overestimates the cost).
- Uses heuristics to guide the search.

#### Advantages:
- Combines efficiency and optimality.
- Adapts to various scenarios through different heuristics.

#### Disadvantages:
- Requires additional computation for the heuristic.
- Performance depends on the quality of the heuristic.

---

## Performance Comparison

The following table summarizes the performance of the algorithms based on runtime, memory usage, and the number of nodes expanded in a specific grid configuration:

| Algorithm              | Runtime (s) | Memory (KB) | Nodes Expanded |
|------------------------|-------------|-------------|----------------|
| DFS                    | 0.000161    | 1.66        | 7              |
| BFS                    | 0.000145    | 1.66        | 7              |
| A* (Manhattan)         | 0.000130    | 0.83        | 7              |
| A* (Euclidean)         | 0.000129    | 0.83        | 7              |

### Analysis:
- **DFS** has the highest runtime, indicating its inefficiency compared to other algorithms in this setup.
- **BFS** performs slightly better than DFS, as it systematically explores nodes level by level.
- **A* Search (both Manhattan and Euclidean heuristics)** outperforms DFS and BFS due to its heuristic-guided exploration, with **Euclidean** being marginally faster.
- **DFS** and **BFS** consume the most memory (1.66 KB), as they store more intermediate nodes during exploration.
- **A*** algorithms require less memory (0.83 KB) because the heuristic effectively limits the nodes that need to be stored and processed.

### Conclusion:
- **DFS** is best for exploring all possible paths, such as puzzle-solving or maze generation, and scenarios where memory usage is limited. However, it is not suitable for finding the shortest path in unweighted grids or graphs, and it can explore redundant paths in dense graphs.
- **BFS** is best for finding the shortest path in unweighted grids or graphs, particularly in routing, communication networks, and social graph applications. However, it is not suitable for large grids or graphs, as it requires significant memory to store all nodes at the current level.
- **A* with Manhattan Distance** is ideal for grids with horizontal and vertical movement (no diagonal movement allowed), such as warehouse navigation or city maps. It is not suitable for grids where diagonal movement is allowed.
- **A* with Euclidean Distance** is best for grids where diagonal movement is allowed, such as robotics or game AI. It is not suitable for grids restricted to cardinal movement only.
