# pylint: disable=all
from collections import deque


class PuzzleState:
    def __init__(self, board, empty_pos, parent=None, move=""):
        self.board = board
        self.empty_pos = empty_pos
        self.parent = parent
        self.move = move

    def generate_children(self):
        children = []
        directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        row, col = self.empty_pos
        for direction, (dr, dc) in directions.items():
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = [row[:] for row in self.board]
                new_board[row][col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[row][col]
                children.append(PuzzleState(new_board, (new_row, new_col), self, direction))
        return children

    def is_goal(self, goal_state):
        return self.board == goal_state

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))

    def __eq__(self, other):
        return self.board == other.board


class PuzzleSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state

    def solve(self):
        initial_state = PuzzleState(self.start_state, self.find_empty(self.start_state))
        queue = deque([initial_state])
        visited = set([initial_state])
        while queue:
            current_state = queue.popleft()
            if current_state.is_goal(self.goal_state):
                return self.backtrack_solution(current_state), len(visited)
            for child in current_state.generate_children():
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
        return None, len(visited)

    def backtrack_solution(self, state):
        moves = []
        while state.parent:
            moves.append(state.move)
            state = state.parent
        return moves[::-1]

    @staticmethod
    def find_empty(board):
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    return row, col


if __name__ == "__main__":
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

    solver = PuzzleSolver(start_board, goal_board)
    solution_moves, steps_explored = solver.solve()

    if solution_moves:
        print(f"Solution found in {len(solution_moves)} moves: {solution_moves}")
        print(f"Total states explored: {steps_explored}")
    else:
        print("No solution found.")