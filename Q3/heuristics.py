import numpy as np


def euclidean(a, b) -> float:
    """
    Calculate the Euclidean distance between two grid nodes.

    Formula:
        sqrt((x1 - x2)^2 + (y1 - y2)^2)

    Args:
        a (tuple[int, int]): Coordinates of the first node.
        b (tuple[int, int]): Coordinates of the second node.

    Returns:
        float: The Euclidean distance between node a and node b.
    """
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def manhattan(a, b) -> int:
    """
    Calculate the Manhattan distance between two grid nodes.

    Formula:
        |x1 - x2| + |y1 - y2|

    Args:
        a (tuple[int, int]): Coordinates of the first node.
        b (tuple[int, int]): Coordinates of the second node.

    Returns:
        int: The Manhattan distance between node a and node b.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def chebyshev(a, b) -> int:
    """
    Calculate the Chebyshev distance between two grid nodes.

    Formula:
        max(|x1 - x2|, |y1 - y2|)

    Args:
        a (tuple[int, int]): Coordinates of the first node.
        b (tuple[int, int]): Coordinates of the second node.

    Returns:
        int: The Chebyshev distance between node a and node b.
    """
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def octile(a, b) -> float:
    """
    Calculate the Octile distance between two grid nodes.

    Formula:
        max(dx, dy) + (sqrt(2) - 1) * min(dx, dy)

    Args:
        a (tuple[int, int]): Coordinates of the first node.
        b (tuple[int, int]): Coordinates of the second node.

    Returns:
        float: The Octile distance between node a and node b.
    """
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return max(dx, dy) + (np.sqrt(2) - 1) * min(dx, dy)
