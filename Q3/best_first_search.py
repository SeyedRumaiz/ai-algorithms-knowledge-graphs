import heapq
from search_algorithm import SearchAlgorithm


class BestFirstSearch(SearchAlgorithm):
    """
    Implementation of the Best-First Search algorithm.

    This search strategy expands the node that appears closest to the
    goal according to a heuristic function. The heuristic function
    estimates the distance between a node and the goal.
    """
    def __init__(self, maze, start, goal, heuristic) -> None:
        """
        Initializes the Best-First Search algorithm.

        Args:
            maze (list[list[int]]):
                The maze grid where valid cells can be traversed.

            start (tuple[int, int]):
                Coordinates of the starting node in the maze.

            goal (tuple[int, int]):
                Coordinates of the goal node.

            heuristic (callable):
                A function that estimates the distance between
                two nodes. Used to prioritize which node to explore next.
        """
        super().__init__(maze, start, goal)
        self.heuristic = heuristic


    def search(self):
        """
        Performs the Greedy Best-First Search algorithm.

        It expands the node that looks closest to the goal using
        a distance heuristic.

        Returns:
            visited_order (list[tuple[int, int]]):
                List of nodes explored during the search.

            time (int):
                Number of nodes visited in the search.

            result (list[tuple[int, int]] | None):
                The path from start node to the goal node if
                a solution exists.

            total_cost (float | None):
                Total cost of the solution.

            straight (int | None):
                Number of straight movements in the path.

            diagonal (int | None):
                Number of diagonal movements in the path.
        """

        # Define min-heap to store (priority, node)
        # Priority is the heuristic distance to the goal
        open_list = []

        # Insert the start node with its heuristic priority
        heapq.heappush(open_list, (self.heuristic(self.start, self.goal), self.start))

        # Path reconstruction dictionary
        came_from = {self.start: None}  # Child-parent mapping
        visited = set()  # Nodes already expanded
        visited_order = []  # Visited order of nodes
        time = 0

        # Loop until goal is found or the heap is empty (no path exists)
        while open_list:

            # Pick the smallest heuristic node
            _, current = heapq.heappop(open_list)

            # Skip nodes that have already been expanded
            if current in visited:
                continue

            # Mark as explored and record order of explored nodes
            visited.add(current)
            visited_order.append(current)
            time += 1  # For sum of all nodes explored (total time)

            # Goal test
            if current == self.goal:
                path = []  # Reconstruct path if reached goal
                while current:
                    path.append(current)
                    current = came_from[current]  # Start from goal then goes to parent

                total_cost, straight, diagonal = self.get_cost(path)
                return visited_order, time, path[::-1], total_cost, straight, diagonal  # Reverse so it is start to goal

            # Check all neighbors in all 8 directions
            neighbors = []
            for dx, dy in self.DIRECTIONS:
                neighbor = (current[0] + dx, current[1] + dy)

                if (self.is_valid(self.maze, neighbor) and
                        neighbor not in visited and
                        neighbor not in came_from):  # Prevents overwriting parent + duplicates
                    neighbors.append(neighbor)

            # Since neighbors processed in increasing node ID (consistent ordering)
            neighbors.sort(key=self.to_node_id)

            for neighbor in neighbors:
                came_from[neighbor] = current

                # Push into queue with chebyshev as the priority
                heapq.heappush(open_list, (self.heuristic(neighbor, self.goal), neighbor))

        return visited_order, time, None, None, None, None  # If no path exists
