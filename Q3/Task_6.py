import numpy as np
import random

from heuristics import euclidean, manhattan, octile
from visualizations import visualize_path, plot, show_summary_run
from best_first_search import BestFirstSearch
from iterative_deepening_DFS import IterativeDeepeningDFS
from maze_utils import generate_maze, generate_coordinates


N_RUNS = 3
SEED = 42

heuristics = {
    "Euclidean": euclidean,
    "Manhattan": manhattan,
    "Octile": octile
}

# Generate the same runs once
random.seed(SEED)

runs = []

# Generate 3 random mazes
for i in range(N_RUNS):
    start_coords, goal_coords = generate_coordinates()
    maze, barriers = generate_maze(start_coords, goal_coords)
    runs.append((maze, barriers, start_coords, goal_coords))


iddfs_times = []
iddfs_lengths = []


for i, (maze, barriers, start_coords, goal_coords) in enumerate(runs, start=1):
    iddfs = IterativeDeepeningDFS(maze, start_coords, goal_coords)

    (iddfs_total_visited, iddfs_time, iddfs_result,
     iddfs_total_cost, iddfs_straight, iddfs_diagonal) = iddfs.search()

    iddfs_times.append(iddfs_time)
    iddfs_lengths.append(len(iddfs_result) if iddfs_result else 0)

    show_summary_run(start_coords, goal_coords, barriers, iddfs_total_visited,
                     iddfs_time, iddfs_result, iddfs_total_cost,
                     iddfs_straight, iddfs_diagonal,
                     title=f"IDDFS - Run {i} Summary")

    visualize_path(maze, iddfs_result, start_coords, goal_coords, title=f"IDDFS path (Run {i})")

iddfs_mean_time = float(np.mean(iddfs_times))
iddfs_var_time  = float(np.var(iddfs_times))
iddfs_mean_len  = float(np.mean(iddfs_lengths))
iddfs_var_len   = float(np.var(iddfs_lengths))

# Run BestFS for each heuristic on the same runs
items = {}

bestfs_stats_by_heuristic = {}     # For plotting across heuristics


for h_name, h_fn in heuristics.items():
    best_times = []
    best_lengths = []

    for i, (maze, barriers, start_coords, goal_coords) in enumerate(runs, start=1):
        best_first_search = BestFirstSearch(maze, start_coords, goal_coords, heuristic=h_fn)

        (best_total_visited, best_time, best_result,
         best_total_cost, best_straight, best_diagonal) = best_first_search.search()

        best_times.append(best_time)
        best_lengths.append(len(best_result) if best_result else 0)

        show_summary_run(start_coords, goal_coords, barriers, best_total_visited,
                         best_time, best_result, best_total_cost,
                         best_straight, best_diagonal,
                         title=f"BestFS ({h_name}) - Run {i} Summary")

        visualize_path(maze, best_result, start_coords, goal_coords, title=f"BestFS {h_name} path (Run {i})")

    # BestFS stats for this heuristic
    best_mean_time = float(np.mean(best_times))
    best_var_time  = float(np.var(best_times))
    best_mean_len  = float(np.mean(best_lengths))
    best_var_len   = float(np.var(best_lengths))

    # Save for summary table
    items[h_name] = (
        iddfs_mean_time, iddfs_var_time, iddfs_mean_len, iddfs_var_len,
        best_mean_time,  best_var_time,  best_mean_len,  best_var_len
    )

    bestfs_stats_by_heuristic[h_name] = {
        "mean_time": best_mean_time,
        "var_time": best_var_time,
        "mean_len": best_mean_len,
        "var_len": best_var_len
    }

    # Per heuristic comparison plots
    plot(iddfs_mean_time, best_mean_time,
         title=f"Mean Solution Time: IDDFS vs BestFS ({h_name})",
         ylabel="Time",
         filename=f"assets/Task_6/iddfs_bestfs_mean_time_{h_name.lower()}.png")

    plot(iddfs_var_time, best_var_time,
         title=f"Variance of Solution Time: IDDFS vs BestFS ({h_name})",
         ylabel="Variance(Time)",
         filename=f"assets/Task_6/iddfs_bestfs_var_time_{h_name.lower()}.png")

    plot(iddfs_mean_len, best_mean_len,
         title=f"Mean Path Length: IDDFS vs BestFS ({h_name})",
         ylabel="Path Length",
         filename=f"assets/Task_6/iddfs_bestfs_mean_length_{h_name.lower()}.png")

    plot(iddfs_var_len, best_var_len,
         title=f"Variance of Path Length: IDDFS vs BestFS ({h_name})",
         ylabel="Variance(Length)",
         filename=f"assets/Task_6/iddfs_bestfs_var_length_{h_name.lower()}.png")
