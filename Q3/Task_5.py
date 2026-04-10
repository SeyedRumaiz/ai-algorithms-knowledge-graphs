import numpy as np
import random

from visualizations import visualize_path, plot, show_summary_run
from heuristics import chebyshev
from best_first_search import BestFirstSearch
from iterative_deepening_DFS import IterativeDeepeningDFS
from maze_utils import generate_maze, generate_coordinates


# Initialize times and lengths for future statistics
iddfs_times = []
iddfs_lengths = []
best_times = []
best_lengths = []
N_RUNS = 3
SEED = 42   # Seed for reproducibility


random.seed(SEED)

# Perform search using three mazes for the two algorithms
for i in range(N_RUNS):

    # Maze setup
    start_coords, goal_coords = generate_coordinates()
    maze, barriers = generate_maze(start_coords, goal_coords)

    # Perform the searches
    iddfs = IterativeDeepeningDFS(maze, start_coords, goal_coords)
    best_first_search = BestFirstSearch(maze, start_coords, goal_coords, heuristic=chebyshev)

    # Add IDDFS readings
    (iddfs_total_visited, iddfs_time, iddfs_result,
     iddfs_total_cost, iddfs_straight, iddfs_diagonal)\
        = iddfs.search()
    iddfs_times.append(iddfs_time)
    iddfs_lengths.append(len(iddfs_result) if iddfs_result else 0)

    # View IDDFS statistics and final path
    show_summary_run(start_coords, goal_coords, barriers, iddfs_total_visited,
                     iddfs_time, iddfs_result, iddfs_total_cost,
                    iddfs_straight, iddfs_diagonal,
                     title=f"Iterative Deepening DFS - Run {i+1} Summary")

    visualize_path(maze, iddfs_result, start_coords, goal_coords, title="IDDFS path")

    # Add BestFS readings
    (best_total_visited, best_time, best_result,
     best_total_cost, best_straight, best_diagonal) = best_first_search.search()
    best_lengths.append(len(best_result) if best_result else 0)
    best_times.append(best_time)

    # View BestFS statistics and final path
    show_summary_run(start_coords, goal_coords, barriers, best_total_visited,
                     best_time, best_result, best_total_cost,
                    best_straight, best_diagonal,
                     title=f"BestFS (Chebyshev) - Run {i+1} Summary")

    visualize_path(maze, best_result, start_coords, goal_coords, title="BestFS path")


# Get mean times for both algorithms
mean_iddfs_time = np.mean(iddfs_times)
mean_best_time = np.mean(best_times)

plot(mean_iddfs_time, mean_best_time, title="Plot of mean times",
     ylabel="Time (minutes)", filename="assets/Task_5/iddfs_bestfs_mean_time.png")

# Variance times for both algorithms
var_iddfs_time = np.var(iddfs_times)
var_best_time = np.var(best_times)

plot(var_iddfs_time, var_best_time, title="Plot of variance times",
     ylabel="Time (minutes)", filename="assets/Task_5/iddfs_bestfs_var_time.png")

# Mean path lengths for both algorithms
mean_iddfs_length = np.mean(iddfs_lengths)
mean_best_length = np.mean(best_lengths)

plot(mean_iddfs_length, mean_best_length, title="Plot of mean lengths",
     ylabel="Length", filename="assets/Task_5/iddfs_bestfs_mean_length.png")

# Variance path lengths for both algorithms
var_iddfs_length = np.var(iddfs_lengths)
var_best_length = np.var(best_lengths)

plot(var_iddfs_length, var_best_length, title="Plot of variance lengths",
     ylabel="Length", filename="assets/Task_5/iddfs_bestfs_var_length.png")
