from visualizations import visualize_path
from heuristics import chebyshev
from best_first_search import BestFirstSearch
from maze_utils import generate_maze, generate_coordinates


def show_bestfs_run(start, goal, barriers, visited, time_taken, path, cost=None,
                    straight=None, diagonal=None):
    print("\n" + "=" * 70)
    print("Greedy Best First Search (Chebyshev) - Run Summary")
    print("=" * 70)
    print(f"Start (x,y)  :  {start}")
    print(f"Goal (x,y)   :  {goal}")
    print(f"Barriers     :  {sorted(barriers)}")
    print(f"Time (mins)  :  {time_taken} (1 min per expanded node)")
    print(f"Visited (#)  :  {len(visited)}")
    if cost is not None:
        print(f"Path cost  :  {cost:.3f}")
    if straight is not None and diagonal is not None:
        print(f"Moves        : straight={straight}, diagonal={diagonal}")

    print("-"*70)
    print(f"Final path (#nodes={len(path)}):")
    print("  " + " -> ".join(map(str, path)))

    print("-"*70)
    print("Visited nodes (prefix):")
    preview = visited[:40]
    print("  " + ", ".join(map(str, preview)) + (" ..." if len(visited) > 40 else ""))
    print("="*70 + "\n")


start_coords, goal_coords = generate_coordinates()
maze, barriers = generate_maze(start_coords, goal_coords)

bestfs = BestFirstSearch(maze, start_coords, goal_coords, heuristic=chebyshev)
visited, time_taken, path, cost, straight, diagonal = bestfs.search()

show_bestfs_run(start_coords, goal_coords, barriers, visited, time_taken, path, cost, straight, diagonal)
visualize_path(maze, path, start_coords, goal_coords,
               f"Path from {start_coords} to {goal_coords} (BestFS Chebyshev)")
