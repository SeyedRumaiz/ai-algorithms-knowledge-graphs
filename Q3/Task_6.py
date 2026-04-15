import numpy as np
import random

from heuristics import euclidean, manhattan, octile
from visualizations import visualize_path, plot, show_summary_run
from best_first_search import BestFirstSearch
from iterative_deepening_DFS import IterativeDeepeningDFS
from maze_utils import generate_maze, generate_coordinates

# Total of 3 runs needed, and ensure reproducibility
N_RUNS = 3
SEED = 42

# Heuristics used
heuristics = {
    "Euclidean": euclidean,
    "Manhattan": manhattan,
    "Octile": octile
}

# Generate the same runs once
random.seed(SEED)

runs = []   # Stores all mazes

# Generate 3 random mazes
for i in range(N_RUNS):
    start_coords, goal_coords = generate_coordinates()
    maze, barriers = generate_maze(start_coords, goal_coords)
    runs.append((maze, barriers, start_coords, goal_coords))

# IDDFS metrics
iddfs_times = []
iddfs_lengths = []
iddfs_cost = []


# Run IDDFS for the mazes
for i, (maze, barriers, start_coords, goal_coords) in enumerate(runs, start=1): # Adjust start for display info
    iddfs = IterativeDeepeningDFS(maze, start_coords, goal_coords)

    (iddfs_total_visited, iddfs_time, iddfs_result,
     iddfs_total_cost, iddfs_straight, iddfs_diagonal) = iddfs.search()

    iddfs_times.append(iddfs_time)
    iddfs_cost.append(iddfs_total_cost)
    iddfs_lengths.append(len(iddfs_result)-1 if iddfs_result else 0)

    show_summary_run(start_coords, goal_coords, barriers, iddfs_total_visited,
                     iddfs_time, iddfs_result, iddfs_total_cost,
                     iddfs_straight, iddfs_diagonal,
                     title=f"IDDFS - Run {i} Summary")

    visualize_path(maze, iddfs_result, start_coords, goal_coords, title=f"IDDFS path (Run {i})")

# Calculate key statistics
iddfs_mean_time = float(np.mean(iddfs_times))
iddfs_var_time  = float(np.var(iddfs_times))
iddfs_mean_cost = float(np.mean(iddfs_cost))
iddfs_var_cost = float(np.var(iddfs_cost))
iddfs_mean_len  = float(np.mean(iddfs_lengths))
iddfs_var_len   = float(np.var(iddfs_lengths))

# Run BestFS for each heuristic on the same runs
items = {}

bestfs_stats_by_heuristic = {}     # For plotting across heuristics


# Loop through all the heuristics
for h_name, h_fn in heuristics.items():
    best_times = []
    best_lengths = []
    best_costs = []

    # Run BestFS for a heuristic
    for i, (maze, barriers, start_coords, goal_coords) in enumerate(runs, start=1):
        best_first_search = BestFirstSearch(maze, start_coords, goal_coords, heuristic=h_fn)

        (best_total_visited, best_time, best_result,
         best_total_cost, best_straight, best_diagonal) = best_first_search.search()

        best_times.append(best_time)
        best_costs.append(best_total_cost)
        best_lengths.append(len(best_result)-1 if best_result else 0)

        show_summary_run(start_coords, goal_coords, barriers, best_total_visited,
                         best_time, best_result, best_total_cost,
                         best_straight, best_diagonal,
                         title=f"BestFS ({h_name}) - Run {i} Summary")

        visualize_path(maze, best_result, start_coords, goal_coords, title=f"BestFS {h_name} path (Run {i})")

    # BestFS stats for this heuristic
    best_mean_time = float(np.mean(best_times))
    best_var_time  = float(np.var(best_times))
    best_mean_cost = float(np.mean(best_costs))
    best_var_cost = float(np.var(best_costs))
    best_mean_len  = float(np.mean(best_lengths))
    best_var_len   = float(np.var(best_lengths))

    # Save for summary table
    items[h_name] = (
        iddfs_mean_time, iddfs_var_time, iddfs_mean_len, iddfs_var_len, iddfs_mean_cost, iddfs_var_cost,
        best_mean_time,  best_var_time,  best_mean_len,  best_var_len, best_mean_cost, best_var_cost
    )

    bestfs_stats_by_heuristic[h_name] = {
        "mean_time": best_mean_time,
        "var_time": best_var_time,
        "mean_cost": best_mean_cost,
        "var_cost": best_var_cost,
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

    plot(iddfs_mean_cost, best_mean_cost,
         title=f"Mean Cost: IDDFS vs BestFS ({h_name})",
         ylabel="Cost",
         filename=f"assets/Task_6/iddfs_bestfs_mean_cost_{h_name.lower()}.png")

    plot(iddfs_var_cost, best_var_cost,
         title=f"Variance of Cost vs BestFS ({h_name})",
         ylabel="Variance(Cost)",
         filename=f"assets/Task_6/iddfs_bestfs_var_cost_{h_name.lower()}.png")

    plot(iddfs_mean_len, best_mean_len,
         title=f"Mean Path Length: IDDFS vs BestFS ({h_name})",
         ylabel="Path Length",
         filename=f"assets/Task_6/iddfs_bestfs_mean_length_{h_name.lower()}.png")

    plot(iddfs_var_len, best_var_len,
         title=f"Variance of Path Length: IDDFS vs BestFS ({h_name})",
         ylabel="Variance(Length)",
         filename=f"assets/Task_6/iddfs_bestfs_var_length_{h_name.lower()}.png")
