from visualizations import visualize_path, show_summary_run
from iterative_deepening_DFS import IterativeDeepeningDFS
from maze_utils import generate_maze, generate_coordinates
import random

random.seed(42)

start_coords, goal_coords = generate_coordinates()
maze, barriers = generate_maze(start_coords, goal_coords)

iddfs = IterativeDeepeningDFS(maze, start_coords, goal_coords)
visited, time_taken, path, cost, straight, diagonal = iddfs.search()

show_summary_run(start_coords, goal_coords, barriers, visited,
                 time_taken, path, cost, straight, diagonal,
                 title="Iterative Deepening DFS - Run Summary")
visualize_path(maze, path, start_coords, goal_coords,
               title=f"Path from {start_coords} to {goal_coords} (IDDFS)")
