import matplotlib.pyplot as plt
import numpy as np


def visualize_path(grid, path, start, goal, title) -> None:
    """
    Visualize the maze grid and the final path found by a search algorithm.

    Args:
        grid (list[list[int]] | np.ndarray):
            2D maze grid where 0 = free cell and 1 = obstacle.

        path (list[tuple[int, int]] | None):
            List of coordinates representing the final path from start to goal.
            If None, only the maze and start/goal will be displayed.

        start (tuple[int, int]):
            Coordinates of the start node (x, y).

        goal (tuple[int, int]):
            Coordinates of the goal node (x, y).

        title (str):
            Title displayed on top of the plot.

    Returns:
        None
    """
    grid_visual = np.array(grid)    # Easier for matplotlib and to get shape

    plt.figure(figsize=(6, 6))
    plt.imshow(grid_visual, cmap="binary", origin="upper")

    # Path is list of (x, y), if available
    if path:
        xs = [x for x, y in path]
        ys = [y for x, y in path]
        plt.plot(xs, ys, color="red", linewidth=2, marker="o", markersize=4)

    # Start/goal are (x, y)
    plt.text(start[0], start[1], "S", ha="center", va="center",
             color="blue", fontweight="bold")
    plt.text(goal[0], goal[1], "G", ha="center", va="center",
             color="green", fontweight="bold")

    rows, cols = grid_visual.shape
    # Hide tick labels
    plt.xticks(range(cols))
    plt.yticks(range(rows))

    # Minor ticks at cell borders (for grid lines)
    plt.xticks(np.arange(-0.5, cols, 1), minor=True)
    plt.yticks(np.arange(-0.5, rows, 1), minor=True)

    plt.grid(which="minor", color="black", linestyle="-", linewidth=1)
    plt.title(title, fontsize=16, fontweight="bold")

    plt.xlim(-0.5, cols - 0.5)
    plt.ylim(rows - 0.5, -0.5)  # Keeps (0,0) at top-left

    plt.show()

def plot(iddfs, best, title, ylabel, filename) -> None:
    """
    Create and save a bar chart comparing two algorithms.

    Args:
        iddfs (Float[Any]):
            Metric value for the IDDFS algorithm.

        best (Float[Any]):
            Metric value for the Best-First Search algorithm.

        title (str):
            Title of the chart.

        ylabel (str):
            Label for the y-axis.

        filename (str):
            File name used to save the figure as an image.

    Returns:
        None
    """
    labels = ["IDDFS", "BestFS"]
    values = [iddfs, best]

    plt.figure(figsize=(6, 5))
    bars = plt.bar(labels, values)

    plt.title(title, fontsize=14, fontweight="bold")
    plt.ylabel(ylabel, fontsize=12)
    plt.xlabel("Algorithm", fontsize=12)

    # Light horizontal grid
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Add numbers above bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=11
        )

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()


def show_summary_run(start, goal, barriers, visited, time_taken, path,
                     cost=None, straight=None, diagonal=None, title=None) -> None:
    """
    Print a formatted console summary of a search algorithm run.

    Args:
        start (tuple[int, int]):
            Start node coordinates.

        goal (tuple[int, int]):
            Goal node coordinates.

        barriers (set[tuple[int, int]]):
            Set of obstacle coordinates in the maze.

        visited (list[tuple[int, int]]):
            Order of nodes expanded during the search.

        time_taken (int):
            Total number of nodes expanded.

        path (list[tuple[int, int]]):
            Final path from start to goal.

        cost (float):
            Total path cost.

        straight (int):
            Number of straight moves in the path.

        diagonal (int):
            Number of diagonal moves in the path.

        title (str):
            Title printed at the top of the summary.

    Returns:
        None
    """
    print("\n" + "=" * 70)
    print(title)
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

    # Prepare a prefix of the visited list (if many nodes present)
    preview = visited[:40]
    print("  " + ", ".join(map(str, preview)) + (" ..." if len(visited) > 40 else ""))
    print("="*70 + "\n")
