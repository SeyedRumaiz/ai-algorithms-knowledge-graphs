from search_algorithm import SearchAlgorithm


class IterativeDeepeningDFS(SearchAlgorithm):

    def __init__(self, maze, start, goal):
        super(IterativeDeepeningDFS, self).__init__(maze, start, goal)


    def search(self):
        """
        Performs iterative deepening depth first search.

        Returns:
            total_visited
            time
            result
        """
        def dls(node, depth, path):
            """
            Performs depth limited search recursively.

            Args:
                node (tuple[int, int]): (x, y) Coordinates of the point.
                depth (int): Depth of recursion.
                path (list): Path of recursion.

            Returns:
                path:
                visited_order
            """

            visited_order = [node]

            if node == self.goal:    # Node is current position, path is list of visited cells along the current route
                return path, visited_order # Full route list
            if depth == 0:
                return None, visited_order

            neighbors = []
            for dx, dy in self.DIRECTIONS:
                next_pos = (node[0] + dx, node[1] + dy)
                if self.is_valid(self.maze, next_pos) and next_pos not in path:
                    neighbors.append(next_pos)

            neighbors.sort(key=self.to_node_id)

            for nxt in neighbors:
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
