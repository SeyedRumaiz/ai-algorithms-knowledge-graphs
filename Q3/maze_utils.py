import random
from typing import List, Tuple


MAX_SIZE = 6

def from_node_id(n) -> Tuple[int, int]:
    """

    Args:
        n:

    Returns:
        Tuple[int, int]:
    """
    x = n // MAX_SIZE    # Column
    y = n % MAX_SIZE   # Row
    return x, y


def generate_coordinates() -> tuple[tuple[int, int], tuple[int, int]]:
    """

    Returns:
         Tuple[int, int]:
    """
    start_id = random.randint(0, 11)
    goal_id = random.randint(24, 35)

    return from_node_id(start_id), from_node_id(goal_id)


def generate_maze(start_coords, goal_coords):
    """

    Args:
        start_coords:
        goal_coords:

    Returns:
        List[List[int]]:
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
