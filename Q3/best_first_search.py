import heapq
from search_algorithm import SearchAlgorithm


class BestFirstSearch(SearchAlgorithm):

    def __init__(self, maze, start, goal, heuristic):
        super(BestFirstSearch, self).__init__(maze, start, goal)
        self.heuristic = heuristic


    def search(self):
        """
        Performs best first search recursively.
        It expands the node that looks closest to the goal using
        a distance heuristic.

        Returns:
            path: Path of recursion.
            time: Time of recursion.
        """

        # Define min-heap tp store tuple (priority, node)
        # where priority is the heuristic
        open_list = []  # Pop the node with smallest heuristic value
        heapq.heappush(open_list, (self.heuristic(self.start, self.goal), self.start))

        # Parent tracking
        came_from = {self.start: None}
        visited = set()  # Nodes already expanded
        visited_order = []  # Visited order of nodes
        time = 0

        # Loop until goal is found or the heap is empty (no path exists)
        while open_list:

            # Pick the smallest heuristic node
            _, current = heapq.heappop(open_list)

            # Skip duplicates (same node from different parents)
            if current in visited:
                continue

            # Mark as explored and record order of explored nodes
            visited.add(current)
            visited_order.append(current)
            time += 1  # For sum of all nodes explored (total time)

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

            # Since neighbors processed in increasing node ID
            neighbors.sort(key=self.to_node_id)

            for neighbor in neighbors:
                came_from[neighbor] = current

                # Push into queue with chebyshev as the priority
                heapq.heappush(open_list, (self.heuristic(neighbor, self.goal), neighbor))

        return visited_order, time, None  # If no path exists
