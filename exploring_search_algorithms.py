import heapq
import time
import tracemalloc
import matplotlib.pyplot as plt


# 1. Environment Setup

def create_grid():
    return [
        ['S', '.', '.', 'X', 'G'],
        ['.', 'X', '.', '.', '.'],
        ['.', 'X', 'X', 'X', '.'],
        ['.', '.', '.', '.', '.']
    ]


def create_graph():
    return {
        'A': [('B', 2), ('C', 4)],
        'B': [('D', 3)],
        'C': [('D', 1), ('G', 6)],
        'D': [('G', 5)],
        'G': []
    }


# 2. Algorithm Implementation

# Depth-First Search
def dfs(grid):
    start, goal = (0, 0), (0, 4)
    stack = [start]
    visited = set()
    parent = {}

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = current

    return reconstruct_path(parent, start, goal)


# Breadth-First Search
def bfs(grid):
    start, goal = (0, 0), (0, 4)
    queue = [start]
    visited = set()
    parent = {}

    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = current

    return reconstruct_path(parent, start, goal)


# A* Search
def a_star(grid, heuristic='manhattan'):
    start, goal = (0, 0), (0, 4)
    open_list = []
    heapq.heappush(open_list, (0, start))
    g_score = {start: 0}
    parent = {}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            break

        for neighbor in get_neighbors(grid, current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                if heuristic == 'manhattan':
                    f_score = tentative_g_score + manhattan_distance(neighbor, goal)
                elif heuristic == 'euclidean':
                    f_score = tentative_g_score + euclidean_distance(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                parent[neighbor] = current

    return reconstruct_path(parent, start, goal)


# Helper Functions
def get_neighbors(grid, position):
    x, y = position
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 'X':
            neighbors.append((nx, ny))
    return neighbors


def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent.get(current)
        if current is None:
            return []  # No path found
    path.append(start)
    path.reverse()
    return path


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


# 3. Path Visualization
def visualize_path(grid, path):
    visual = [row[:] for row in grid]
    for x, y in path:
        if visual[x][y] not in ('S', 'G'):
            visual[x][y] = '*'
    for row in visual:
        print(' '.join(row))


def plot_grid(grid, path, title):
    fig, ax = plt.subplots()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'X':
                ax.add_patch(plt.Rectangle((j, len(grid) - i - 1), 1, 1, color='black'))
            elif (i, j) == (0, 0):  # Start
                ax.add_patch(plt.Rectangle((j, len(grid) - i - 1), 1, 1, color='green'))
            elif (i, j) == (0, 4):  # Goal
                ax.add_patch(plt.Rectangle((j, len(grid) - i - 1), 1, 1, color='red'))
            elif (i, j) in path:
                ax.add_patch(plt.Rectangle((j, len(grid) - i - 1), 1, 1, color='yellow'))
    ax.set_xlim(0, len(grid[0]))
    ax.set_ylim(0, len(grid))
    ax.set_xticks(range(len(grid[0]) + 1))
    ax.set_yticks(range(len(grid) + 1))
    plt.grid(True)
    plt.title(title)
    plt.show()


# 4. Performance Analysis
def analyze_performance(grid, algorithm, *args):
    tracemalloc.start()
    start_time = time.time()
    path = algorithm(grid, *args)
    end_time = time.time()
    memory_usage = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    runtime = end_time - start_time
    expanded_nodes = len(path)
    return runtime, memory_usage, expanded_nodes, path


# Main
if __name__ == "__main__":
    grid = create_grid()
    print("Grid:")
    for row in grid:
        print(' '.join(row))

    print("\nDFS:")
    runtime, memory, nodes, path = analyze_performance(grid, dfs)
    visualize_path(grid, path)
    plot_grid(grid, path, "DFS")
    print(f"Runtime: {runtime:.6f}s, Memory: {memory / 1024:.2f} KB, Nodes expanded: {nodes}")

    print("\nBFS:")
    runtime, memory, nodes, path = analyze_performance(grid, bfs)
    visualize_path(grid, path)
    plot_grid(grid, path, "BFS")
    print(f"Runtime: {runtime:.6f}s, Memory: {memory / 1024:.2f} KB, Nodes expanded: {nodes}")

    print("\nA* (Manhattan):")
    runtime, memory, nodes, path = analyze_performance(grid, a_star, 'manhattan')
    visualize_path(grid, path)
    plot_grid(grid, path, "A* (Manhattan)")
    print(f"Runtime: {runtime:.6f}s, Memory: {memory / 1024:.2f} KB, Nodes expanded: {nodes}")

    print("\nA* (Euclidean):")
    runtime, memory, nodes, path = analyze_performance(grid, a_star, 'euclidean')
    visualize_path(grid, path)
    plot_grid(grid, path, "A* (Euclidean)")
    print(f"Runtime: {runtime:.6f}s, Memory: {memory / 1024:.2f} KB, Nodes expanded: {nodes}")
