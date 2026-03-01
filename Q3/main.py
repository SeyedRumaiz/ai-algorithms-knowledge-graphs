import numpy as np
from visualizations import visualize_path, plot
from heuristics import euclidean, manhattan, octile, chebyshev
from best_first_search import BestFirstSearch
from iterative_deepening_DFS import IterativeDeepeningDFS
from maze_utils import generate_maze, generate_coordinates
import random

start, goal = generate_coordinates()
maze, barriers = generate_maze(start, goal)
print(barriers)
iddfs = IterativeDeepeningDFS(maze, start, goal)

print(maze)

random.seed(42)

print("----------------------------------")


total_visited, time, result, total_cost, straight, diagonal = iddfs.search()
print("All visited:",total_visited)
print("Total time:",time)
print("Shortest path:",result)
if diagonal != 0:
    print(f"Exact cost: {straight} + {diagonal}√2")
else:
    print(f"Exact cost: {straight}")
print("Decimal cost:",total_cost)



visualize_path(maze, result, start, goal)

#
#
# heuristics = {
#     "Euclidean": euclidean,
#     "Manhattan": manhattan,
#     "Octile": octile
# }
#
# items = {}
#
#
#
#
# for heuristic in heuristics:
#
#     iddfs_times = []
#     iddfs_lengths = []
#     best_times = []
#     best_lengths = []
#
#     for i in range(3):
#         start_coords, goal_coords = generate_coordinates()
#         maze = generate_maze(start_coords, goal_coords)
#
#         iddfs = IterativeDeepeningDFS(maze, start_coords, goal_coords)
#         best_first_search = BestFirstSearch(maze, start_coords, goal_coords, heuristic=heuristics[heuristic])
#
#         iddfs_total_visited, iddfs_time, iddfs_result = iddfs.search()
#         iddfs_times.append(iddfs_time)
#         iddfs_lengths.append(len(iddfs_result) if iddfs_result else 0)
#
#         best_total_visited, best_time, best_result = best_first_search.search()
#         best_lengths.append(len(best_result) if best_result else 0)
#         best_times.append(best_time)
#
#         print("Total visited (IDDFS):", iddfs_total_visited)
#         print("Time (IDDFS):", iddfs_time)
#         print("Result (IDDFS):", iddfs_result)
#
#         print("Total visited (BEST):", best_total_visited)
#         print("Time (BEST):", best_time)
#         print("Result (BEST):", best_result)
#
#     items[heuristic] = (np.mean(iddfs_times), np.var(iddfs_times),
#                         np.mean(iddfs_lengths), np.var(iddfs_lengths),
#                         np.mean(best_times), np.var(best_times),
#                         np.mean(best_lengths), np.var(best_lengths),
#                         )
#
# plot_mean_times(items=items, index=4)
# plot_mean_path_lengths(items=items, index=6)
#
# plot_variance(items=items, index=5)
# plot_variance(items=items, index=7)