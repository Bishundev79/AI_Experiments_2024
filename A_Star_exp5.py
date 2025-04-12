# pylint:  disable = all
from queue import PriorityQueue

# Helper function to calculate Manhattan distance (heuristic function)
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# A* algorithm implementation
def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])  # Dimensions of the grid
    open_set = PriorityQueue()  # Priority queue to select nodes based on cost
    open_set.put((0, start))  # Add start node with priority 0
    came_from = {}  # To reconstruct the path
    g_score = {start: 0}  # Cost from start to current node
    f_score = {start: heuristic(start, goal)}  # Estimated cost (f = g + h)

    while not open_set.empty():
        current = open_set.get()[1]  # Get node with lowest f_score

        if current == goal:  # Goal reached, reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        # Explore neighbors (up, down, left, right)
        neighbors = [(current[0] + dx, current[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

        for neighbor in neighbors:
            x, y = neighbor
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0:  # Check boundaries and avoid obstacles
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    open_set.put((f_score[neighbor], neighbor))

    return None  # No path found

# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Starting point
goal = (4, 4)  # Goal point

path = a_star(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")