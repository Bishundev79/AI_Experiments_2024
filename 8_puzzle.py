from collections import deque


# Class to represent the state of the 8-puzzle
class PuzzleState:
    def __init__(self, board, empty_pos, parent=None, move=""):
        """
        Initialize the puzzle state.
        :param board: A 2D list representing the puzzle board
        :param empty_pos: A tuple representing the row and column of the empty space
        :param parent: The parent state from which this state is generated (used for backtracking the solution)
        :param move: The move that led to this state (up, down, left, right)
        """
        self.board = board
        self.empty_pos = empty_pos  # Position of the empty tile
        self.parent = parent  # Parent node (for backtracking the solution)
        self.move = move  # Move that was performed to reach this state

    def generate_children(self):
        """
        Generate all possible child states by moving the empty space up, down, left, or right.
        :return: A list of child PuzzleState objects
        """
        children = []
        directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        row, col = self.empty_pos

        # Generate new states by moving the empty tile in each possible direction
        for direction, (dr, dc) in directions.items():
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:  # Ensure the move is within bounds
                new_board = [row[:] for row in self.board]  # Create a copy of the current board
                # Swap the empty space with the adjacent tile
                new_board[row][col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[row][col]
                # Create a new PuzzleState with the updated board and empty position
                children.append(PuzzleState(new_board, (new_row, new_col), self, direction))

        return children

    def is_goal(self, goal_state):
        """
        Check if the current state is the goal state.
        :param goal_state: The goal configuration of the puzzle
        :return: True if the current board matches the goal state, False otherwise
        """
        return self.board == goal_state

    def __hash__(self):
        """
        Hash function to allow states to be used in sets for visited state tracking.
        The board is converted into a tuple, which is hashable.
        """
        return hash(tuple(tuple(row) for row in self.board))

    def __eq__(self, other):
        """
        Equality comparison between two puzzle states (needed for hash comparison).
        """
        return self.board == other.board


class PuzzleSolver:
    def __init__(self, start_state, goal_state):
        """
        Initialize the solver with a starting and goal state.
        :param start_state: The initial configuration of the puzzle
        :param goal_state: The goal configuration of the puzzle
        """
        self.start_state = start_state
        self.goal_state = goal_state

    def solve(self):
        """
        Solve the 8-puzzle problem using BFS.
        :return: A tuple containing the sequence of moves and the number of steps
        """
        # Create the initial state
        initial_state = PuzzleState(self.start_state, self.find_empty(self.start_state))

        # BFS setup: queue and visited set
        queue = deque([initial_state])
        visited = set([initial_state])

        while queue:
            current_state = queue.popleft()

            # Check if we've reached the goal
            if current_state.is_goal(self.goal_state):
                return self.backtrack_solution(current_state), len(visited)

            # Generate children (possible moves) and add to the queue if not visited
            for child in current_state.generate_children():
                if child not in visited:
                    queue.append(child)
                    visited.add(child)

        return None, len(visited)

    def backtrack_solution(self, state):
        """
        Backtrack from the goal state to the start state to get the sequence of moves.
        :param state: The goal state
        :return: A list of moves that led to the solution
        """
        moves = []
        while state.parent:
            moves.append(state.move)
            state = state.parent
        return moves[::-1]  # Reverse to get the correct order

    @staticmethod
    def find_empty(board):
        """
        Find the position of the empty tile (represented by 0) in the puzzle board.
        :param board: A 2D list representing the puzzle board
        :return: A tuple (row, col) representing the position of the empty tile
        """
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    return row, col


# Example usage
if __name__ == "__main__":
    # Define the start and goal configurations
    start_board = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    goal_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    # Create the solver and solve the puzzle
    solver = PuzzleSolver(start_board, goal_board)
    solution_moves, steps_explored = solver.solve()

    if solution_moves:
        print(f"Solution found in {len(solution_moves)} moves: {solution_moves}")
        print(f"Total states explored: {steps_explored}")
    else:
        print("No solution found.")