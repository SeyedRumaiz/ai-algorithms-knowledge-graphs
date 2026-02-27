import random
from typing import List, Tuple

MAX_SIZE = 6


def from_node_id(n: int) -> Tuple[int, int]:
    """
    Convert a node ID into (x, y) coordinates by column-major numbering.

    Args:
        n (int): Node ID in the range [0, 35]

    Returns:
        Tuple[int, int]: (x,y) coordinates where
            x represents the column index,
            y represents the row index.
    """
    x = n // MAX_SIZE    # Column
    y = n % MAX_SIZE   # Row
    return x, y


def generate_coordinates() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Randomly generate start and goal coordinates.

    Returns:
         Tuple[Tuple[int, int], Tuple[int, int]]:
            A tuple containing:
            start_coords (x,y)
            goal_coords (x,y)
    """
    start_id = random.randint(0, 11)
    goal_id = random.randint(24, 35)

    return from_node_id(start_id), from_node_id(goal_id)


def generate_maze(start_coords: Tuple[int, int],
                  goal_coords: Tuple[int, int]) -> Tuple[List[List[int]], set]:
    """
    Generate a 6x6 maze with randomly placed barrier nodes.

    Rules:
    - Start node is selected from IDs 0–11 (left two columns).
    - Goal node is selected from IDs 24–35 (right two columns).

    The maze is represented as a 2D grid:
    0 → free cell
    1 → barrier cell

    Four barrier nodes are randomly selected such that:
        - They do not overlap with the start node.
        - They do not overlap with the goal node.

    Args:
        start_coords (Tuple[int, int]): Coordinates of the start node.
        goal_coords (Tuple[int, int]): Coordinates of the goal node.

    Returns:
        Tuple[List[List[int]], set]:
            maze (List[List[int]]): 2D representation of the maze.
            barriers (set): Set of barrier coordinate tuples (x,y)
    """
    maze = [[0] * 6 for _ in range(6)]
    barriers = set()

    while len(barriers) < 4:
        barrier_row = random.randint(0, 5)
        barrier_column = random.randint(0, 5)

        barrier = (barrier_column, barrier_row)

        # Barrier cannot be the goal or the start
        if barrier == goal_coords or barrier == start_coords:
            continue
        barriers.add(barrier)

    for (x, y) in barriers:
        maze[y][x] = 1

    return maze, barriers
