import numpy as np
from abc import ABC, abstractmethod


class SearchAlgorithm(ABC):
    """
    Abstract class for a search algorithm.
    """

    def __init__(self, maze, start, goal):
        """

        :param maze:
        :param start:
        :param goal:
        """
        self.maze = maze
        self.start = start
        self.goal = goal
        self.DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
        self.MAX_SIZE = 6


    @abstractmethod
    def search(self):
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

        Args:
            grid (numpy.ndarray): Grid of point.
            pos (tuple[int, int]): (x, y) Coordinates of the point.
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
        Calculates the cost of the path.

        :param path:
        :return:
        """
        n_iter = len(path) - 1
        total_cost = 0
        straight = 0
        diagonal = 0

        for i in range(n_iter):
            tup = path[i]
            tup_next = path[i + 1]
            dx = abs(tup[0] - tup_next[0])
            dy = abs(tup[1] - tup_next[1])

            if dx == 1 and dy == 1:
                diagonal += 1
            else:
                straight += 1

            cost = np.sqrt(dx**2 + dy**2)
            total_cost += cost
        return total_cost, straight, diagonal
