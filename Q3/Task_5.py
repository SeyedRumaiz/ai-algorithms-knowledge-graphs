import numpy as np
import random

from visualizations import visualize_path, plot
from heuristics import chebyshev
from best_first_search import BestFirstSearch
from iterative_deepening_DFS import IterativeDeepeningDFS
from maze_utils import generate_maze, generate_coordinates


iddfs_times = []
iddfs_lengths = []
best_times = []
best_lengths = []

print("="*50)

random.seed(42)


for i in range(3):
    print("="*50)
    print(f"Running for {i+1}-th run")
    start_coords, goal_coords = generate_coordinates()
    maze, barriers = generate_maze(start_coords, goal_coords)

    iddfs = IterativeDeepeningDFS(maze, start_coords, goal_coords)
    best_first_search = BestFirstSearch(maze, start_coords, goal_coords, heuristic=chebyshev)

    (iddfs_total_visited, iddfs_time, iddfs_result,
     iddfs_total_cost, iddfs_straight, iddfs_diagonal)\
        = iddfs.search()
    iddfs_times.append(iddfs_time)
    iddfs_lengths.append(len(iddfs_result) if iddfs_result else 0)

    visualize_path(maze, iddfs_result, start_coords, goal_coords, title="IDDFS path")

    (best_total_visited, best_time, best_result,
     best_total_cost, best_straight, best_diagonal) = best_first_search.search()
    best_lengths.append(len(best_result) if best_result else 0)
    best_times.append(best_time)

    visualize_path(maze, best_result, start_coords, goal_coords, title="BestFS path")
    print("="*50)

    print("Total visited (IDDFS):", iddfs_total_visited)
    print("Time (IDDFS):", iddfs_time)
    print("Result (IDDFS):", iddfs_result)

    print("Total visited (BEST):", best_total_visited)
    print("Time (BEST):", best_time)
    print("Result (BEST):", best_result)


mean_iddfs_time = np.mean(iddfs_times)
mean_best_time = np.mean(best_times)

plot(mean_iddfs_time, mean_best_time, title="Plot of mean times",
     ylabel="Time (minutes)", filename="iddfs_bestfs_mean_time.png")


var_iddfs_time = np.var(iddfs_times)
var_best_time = np.var(best_times)

plot(var_iddfs_time, var_best_time, title="Plot of variance times",
     ylabel="Time (minutes)", filename="iddfs_bestfs_var_time.png")

print("="*50)


mean_iddfs_length = np.mean(iddfs_lengths)
mean_best_length = np.mean(best_lengths)

plot(mean_iddfs_length, mean_best_length, title="Plot of mean lengths",
     ylabel="Length", filename="iddfs_bestfs_mean_length.png")

var_iddfs_length = np.var(iddfs_lengths)
var_best_length = np.var(best_lengths)

plot(var_iddfs_length, var_best_length, title="Plot of variance lengths",
     ylabel="Length", filename="iddfs_bestfs_var_length.png")
