from visualizations import visualize_path, show_summary_run
from heuristics import chebyshev
from best_first_search import BestFirstSearch
from maze_utils import generate_maze, generate_coordinates
import random

# Seed for reproducibility
SEED = 42
random.seed(SEED)

# Generate the coordinates and the maze
start_coords, goal_coords = generate_coordinates()
maze, barriers = generate_maze(start_coords, goal_coords)

# Perform Best-First Search
bestfs = BestFirstSearch(maze, start_coords, goal_coords, heuristic=chebyshev)
visited, time_taken, path, cost, straight, diagonal = bestfs.search()

# View summary statistics and final path
show_summary_run(start_coords, goal_coords, barriers, visited,
                 time_taken, path, cost, straight, diagonal,
                 title="Greedy Best First Search (Chebyshev) - Run Summary")
visualize_path(maze, path, start_coords, goal_coords,
               title=f"Path from {start_coords} to {goal_coords} (BestFS Chebyshev)")
