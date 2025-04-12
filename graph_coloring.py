# pylint: disable=all
class GraphColoring:
    def __init__(self, graph, num_colors, color_names):
        self.graph = graph
        self.num_colors = num_colors
        self.color_names = color_names
        self.num_vertices = len(graph)
        self.colors = [-1] * self.num_vertices

    # Check if the current color assignment is safe for vertex v
    def is_safe(self, v, color):
        for i in range(self.num_vertices):
            if self.graph[v][i] == 1 and self.colors[i] == color:
                return False
        return True

    # A utility function to solve the graph coloring problem using backtracking
    def graph_coloring_util(self, v):
        if v == self.num_vertices:
            return True

        for color in range(self.num_colors):
            if self.is_safe(v, color):
                self.colors[v] = color

                if self.graph_coloring_util(v + 1):
                    return True

                self.colors[v] = -1  # Backtrack

        return False

    # Solve the graph coloring problem
    def solve(self):
        if self.graph_coloring_util(0):
            self.print_solution()
        else:
            print("Solution does not exist")

    # Print the color assignment
    def print_solution(self):
        print("Color assignments for vertices:")
        for v in range(self.num_vertices):
            print(f"Vertex {v} --> {self.color_names[self.colors[v]]}")


# Example graph represented as an adjacency matrix
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

# List of color names
color_names = ["Red", "Green", "Blue"]

num_colors = len(color_names)  # Number of colors available
gc = GraphColoring(graph, num_colors, color_names)
gc.solve()