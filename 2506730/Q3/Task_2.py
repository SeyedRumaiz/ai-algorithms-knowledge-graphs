from visualizations import visualize_path, show_summary_run
from iterative_deepening_DFS import IterativeDeepeningDFS
from maze_utils import generate_maze, generate_coordinates
import random

# Seed to ensure reproducibility
SEED = 42
random.seed(SEED)

# Generate the coordinates
start_coords, goal_coords = generate_coordinates()

# Generate the maze
maze, barriers = generate_maze(start_coords, goal_coords)

# Perform IDDFS
iddfs = IterativeDeepeningDFS(maze, start_coords, goal_coords)
visited, time_taken, path, cost, straight, diagonal = iddfs.search()

# View summary statistics and final path
show_summary_run(start_coords, goal_coords, barriers, visited,
                 time_taken, path, cost, straight, diagonal,
                 title="Iterative Deepening DFS - Run Summary")
visualize_path(maze, path, start_coords, goal_coords,
               title=f"Path from {start_coords} to {goal_coords} (IDDFS)")
