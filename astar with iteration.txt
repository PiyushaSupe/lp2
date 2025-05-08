import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (row, col)
        self.parent = parent  # Parent node
        self.g = g  # Cost from start
        self.h = h  # Heuristic cost
        self.f = g + h  # Total cost
    
    def __lt__(self, other):
        return self.f < other.f  # Priority queue based on f-score

def heuristic(a, b):
    """Calculate Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_search(maze, start, goal):
    """Perform A* search on the maze."""
    open_list = []  # Priority queue
    closed_set = set()  # Visited nodes
    
    # Start node
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    
    # Movement directions (Up, Down, Left, Right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    iteration = 0  # Step counter
    
    while open_list:
        iteration += 1
        current_node = heapq.heappop(open_list)  # Node with lowest f-score
        
        print(f"\nIteration {iteration}: Exploring {current_node.position}, f={current_node.f}, g={current_node.g}, h={current_node.h}")

        if current_node.position == goal:
            print("\nPath found!")
            return reconstruct_path(current_node)
        
        closed_set.add(current_node.position)

        for direction in directions:
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

def print_maze_with_path(maze, path):
    """Print the maze with the found path."""
    maze_copy = [row[:] for row in maze]  # Create a copy to modify
    for r, c in path:
        maze_copy[r][c] = "*"
    
    for row in maze_copy:
        print(" ".join(str(cell) for cell in row))

# Define the maze (0 = open path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

# Start and Goal positions
start = (0, 0)
goal = (4, 5)

# Run A* Search
path = astar_search(maze, start, goal)

# Print final path
if path:
    print("\nFinal Path:")
    print_maze_with_path(maze, path)
