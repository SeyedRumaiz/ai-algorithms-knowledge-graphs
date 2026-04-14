import numpy as np
from abc import ABC, abstractmethod


class SearchAlgorithm(ABC):
    """
    Abstract class for a search algorithm.
    """

    def __init__(self, maze, start, goal):
        """
        Initializes the search algorithm.

        Args:
            maze: The maze to search.
            start: The starting point.
            goal: The goal point.
        """
        self.maze = maze
        self.start = start
        self.goal = goal
        self.DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
        self.MAX_SIZE = 6


    @abstractmethod
    def search(self):
        """
        Abstract method to be implemented by subclasses.
        """
        pass

    def in_bounds(self, pos, grid) -> bool:
        """
        Checks if a point is within the bounds of the grid.

        Args:
            pos (tuple[int, int]): (x, y) Coordinates of the point
            grid (numpy.ndarray): Grid of point

        Returns:
            bool: True if point is within the bounds of the grid.
        """
        x, y = pos
        return 0 <= y < len(grid) and 0 <= x < len(grid[0])

    def is_free(self, grid, pos) -> bool:
        """
        Checks if a point is free.
        Extracts the x and y coordindaes at a position and checks if it's free.

        Args:
            grid (numpy.ndarray): Grid of point.
            pos (tuple[int, int]): (x, y) Coordinates of the point.

        Returns:
            bool: True if the point is free.
        """
        x, y = pos
        return grid[y][x] == 0

    def to_node_id(self, pos: tuple[int, int]) -> int:
        """
        Converts a point to a node id.

        Args:
            pos (tuple[int, int]): (x, y) Coordinates of the point.

        Returns:
            int: Node id.
        """
        x, y = pos
        return x * self.MAX_SIZE + 6

    def is_valid(self, grid: np.ndarray, position: tuple[int, int]) -> bool:
        """
        Checks if a point is within the bounds of the grid.
        It also checks th current position is free.

        Args:
            grid (numpy.ndarray): Grid of point.
            position (tuple[int, int]): (x, y) Coordinates of the point.

        Returns:
            bool: True if the point is within the bounds of the grid and is free.
        """
        return self.in_bounds(position, grid) and self.is_free(grid, position)


    def get_cost(self, path):
        """
        Computes the cost of a path.

        Straight move cost = 1
        Diagonal move cost = √2

        Args:
            path (list[tuple[int, int]]):
                Sequence of coordinates from start to goal.

        Returns:
            tuple:
                total_cost (float): Sum of movement costs.
                straight (int): Number of straight moves.
                diagonal (int): Number of diagonal moves.
        """

        # Number of moves = number of nodes - 1
        n_iter = len(path) - 1
        total_cost = 0
        straight = 0        # Number of straight paths
        diagonal = 0        # Number of diagonal paths

        # Loop through all possibles moves
        for i in range(n_iter):
            tup = path[i]
            tup_next = path[i + 1]

            # Compare the coordinates
            dx = abs(tup[0] - tup_next[0])
            dy = abs(tup[1] - tup_next[1])

            # Detect movement type
            if dx == 1 and dy == 1:
                diagonal += 1
            else:
                straight += 1

            # Euclidean movement cost
            cost = np.sqrt(dx**2 + dy**2)

            # Increment total cost
            total_cost += cost
        return total_cost, straight, diagonal
