import heapq
import random
import matplotlib.pyplot as plt
import numpy as np

# Define movement directions (Up, Down, Left, Right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g  # Cost from start
        self.h = h  # Estimated cost to goal
        self.f = g + h  # Total estimated cost

    def __lt__(self, other):
        return self.f < other.f  # Priority queue sorting

def heuristic(a, b):
    """Calculate Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_search(maze, start, goal):
    """Perform A* search on the maze."""
    open_list = []  # Priority queue
    closed_set = set()  # Visited nodes
    
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    
    iteration = 0  # Step counter
    
    while open_list:
        iteration += 1
        current_node = heapq.heappop(open_list)  # Node with lowest f-score
        
        print(f"\nIteration {iteration}: Exploring {current_node.position}, f={current_node.f}, g={current_node.g}, h={current_node.h}")

        if current_node.position == goal:
            print("\nPath found!")
            return reconstruct_path(current_node)
        
        closed_set.add(current_node.position)

        for direction in DIRECTIONS:
            new_pos = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])

            if not (0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[0])):
                continue  # Skip out-of-bounds

            if maze[new_pos[0]][new_pos[1]] == 1 or new_pos in closed_set:
                continue  # Skip walls and visited nodes

            g_new = current_node.g + 1
            h_new = heuristic(new_pos, goal)
            new_node = Node(new_pos, current_node, g_new, h_new)
            
            heapq.heappush(open_list, new_node)
            print(f"  Adding {new_pos} to queue with f={new_node.f} (g={new_node.g}, h={new_node.h})")
    
    print("\nNo path found!")
    return None

def reconstruct_path(node):
    """Reconstruct the path from goal to start."""
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]  # Reverse the path

def generate_maze(rows, cols, obstacles):
    """Generate a maze with random obstacles."""
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Place obstacles randomly
    for _ in range(obstacles):
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        maze[x][y] = 1

    # Ensure start and goal positions are open
    maze[0][0] = 0
    maze[rows-1][cols-1] = 0
    return maze

def print_maze(maze):
    """Print the maze."""
    for row in maze:
        print(" ".join(str(cell) for cell in row))

def plot_maze(maze, path):
    """Plot the maze with the found path."""
    rows, cols = len(maze), len(maze[0])
    grid = np.array(maze)

    fig, ax = plt.subplots()
    ax.imshow(grid, cmap="gray_r")

    # Mark the path
    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_y, path_x, marker="o", color="red", markersize=5, linestyle="-", label="Path")

    # Start and Goal markers
    ax.plot(0, 0, marker="o", color="green", markersize=8, label="Start")
    ax.plot(cols-1, rows-1, marker="o", color="blue", markersize=8, label="Goal")

    ax.legend()
    plt.show()

# User inputs
rows, cols = 10, 10
obstacles = int(input("Enter number of obstacles: "))

# Generate maze and print
maze = generate_maze(rows, cols, obstacles)
print("\nGenerated Maze:")
print_maze(maze)

# Define Start and Goal positions
start = (0, 0)
goal = (rows - 1, cols - 1)

# Run A* Search
path = astar_search(maze, start, goal)

# Plot final path
if path:
    print("\nFinal Path Found:")
    plot_maze(maze, path)
else:
    print("\nNo valid path found.")
