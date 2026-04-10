from search_algorithm import SearchAlgorithm


class IterativeDeepeningDFS(SearchAlgorithm):
    """
    Performs iterative deepening depth first search.
    """
    def __init__(self, maze, start, goal) -> None:
        """
        Initializes the IterativeDeepeningDFS algorithm.

        Args:
            maze (list[list[int]]):
                The maze grid where valid cells can be traversed.

            start (tuple[int, int]):
                Coordinates of the starting node in the maze.

            goal (tuple[int, int]):
                Coordinates of the goal node.
        """
        super().__init__(maze, start, goal)


    def search(self):
        """
        Performs iterative deepening depth first search.

        Returns:
            total_visited (list[tuple[int, int]]):
                List of nodes visited in the recursion.
            time (int):
                Number of nodes visited in the search.
            result (list[tuple[int, int]] | None):
                The path from start node to the goal node if
                a solution exists.
            total_cost (float):
                Total cost of the solution.
            straight (int):
                Number of straight movements in the path.
            diagonal (int):
                Number of diagonal movements in the path.
        """
        def dls(node, depth, path):
            """
            Performs depth limited search recursively.
            Needed since DLS is only needed as part of IDDFS.

            Args:
                node (tuple[int, int]): (x, y) Coordinates of the point.
                depth (int): Depth of recursion.
                path (list): Path of recursion.

            Returns:
                path: If goal is found, else None.
                visited_order: Order of nodes visited in the recursion.
            """

            visited_order = [node]  # Visited list

            # Goal test
            if node == self.goal:    # Node is current position, path is list of visited cells along the current route
                return path, visited_order # Full route list

            # Check if depth limit was reached and goal was not to be found
            if depth == 0:
                return None, visited_order

            # Build neighbors list
            neighbors = []

            # Find all possible next moves from current node
            for dx, dy in self.DIRECTIONS:
                next_pos = (node[0] + dx, node[1] + dy)
                if self.is_valid(self.maze, next_pos) and next_pos not in path:
                    neighbors.append(next_pos)

            neighbors.sort(key=self.to_node_id)

            # Core of the recursion - explores each neighbors recursively
            for nxt in neighbors:

                # Create a new list without modification to the old one
                    result, child_visited = dls(nxt, depth - 1, path + [nxt])  # Recurse deeper
                    visited_order.extend(child_visited)
                    if result is not None:
                        return result, visited_order   # If recursive found a path

            return None, visited_order # If none of the moves lead to the goal within this depth

        depth = 0
        total_visited = []

        max_depth = self.MAX_SIZE * self.MAX_SIZE

        while depth <= max_depth: # keep increasing depth until it finds a path
            result, visited_this_depth = dls(self.start, depth, [self.start]) # if no path, it will never stop
            total_visited.extend(visited_this_depth)

            if result is not None:
                time = len(total_visited)
                total_cost, straight, diagonal = self.get_cost(path=result)
                return total_visited, time, result, total_cost, straight, diagonal   # if path found, stop iddfs
            depth += 1  # else increase depth by 1
        return total_visited, len(total_visited), None, None, None, None
