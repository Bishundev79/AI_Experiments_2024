# pylint: disable=all
from collections import deque


def water_jug_BFS(x, y, z):
    visited = set()
    queue = deque([(0, 0)])  # Initial state: both jugs are empty

    while queue:
        jug_a, jug_b = queue.popleft()  # Get the current state

        # Check if either jug contains the desired amount or their sum equals the desired amount
        if jug_a == z or jug_b == z or jug_a + jug_b == z:
            return True

        # Skip if this state has already been visited
        if (jug_a, jug_b) in visited:
            continue

        visited.add((jug_a, jug_b))

        # Fill Jug A
        if jug_a < x:
            queue.append((x, jug_b))

        # Fill Jug B
        if jug_b < y:
            queue.append((jug_a, y))

        # Empty Jug A
        if jug_a > 0:
            queue.append((0, jug_b))

        # Empty Jug B
        if jug_b > 0:
            queue.append((jug_a, 0))

        # Pour from Jug A to Jug B
        if jug_a + jug_b >= y:
            queue.append((jug_a - (y - jug_b), y))
        else:
            queue.append((0, jug_a + jug_b))

        # Pour from Jug B to Jug A
        if jug_a + jug_b >= x:
            queue.append((x, jug_b - (x - jug_a)))
        else:
            queue.append((jug_a + jug_b, 0))

    return False


# Parameters
x = 4  # Capacity of Jug A
y = 3  # Capacity of Jug B
z = 2  # Desired amount of water

# Solution
if water_jug_BFS(x, y, z):
    print(f'You can measure {z} liters of water using {x}-liter and {y}-liter jugs.')
else:
    print(f'You cannot measure {z} liters of water using {x}-liter and {y}-liter jugs.')
