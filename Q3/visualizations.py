import matplotlib.pyplot as plt
import numpy as np

def visualize_path(grid, path, start, goal):
    grid_visual = np.array(grid)

    plt.figure(figsize=(6, 6))
    plt.imshow(grid_visual, cmap="binary", origin="upper")

    # path is list of (x, y)
    if path:
        xs = [x for x, y in path]
        ys = [y for x, y in path]
        plt.plot(xs, ys, color="red", linewidth=2, marker="o", markersize=4)

    # start/goal are (x, y)
    plt.text(start[0], start[1], "S", ha="center", va="center",
             color="blue", fontweight="bold")
    plt.text(goal[0], goal[1], "G", ha="center", va="center",
             color="green", fontweight="bold")

    rows, cols = grid_visual.shape
    # Hide tick labels (optional, but clean)
    plt.xticks(range(cols))
    plt.yticks(range(rows))

    # Minor ticks at cell borders (for grid lines)
    plt.xticks(np.arange(-0.5, cols, 1), minor=True)
    plt.yticks(np.arange(-0.5, rows, 1), minor=True)

    plt.grid(which="minor", color="black", linestyle="-", linewidth=1)
    plt.title(f"Navigation from {start} to {goal} using IDDFS", fontsize=16, fontweight="bold")

    plt.xlim(-0.5, cols - 0.5)
    plt.ylim(rows - 0.5, -0.5)  # keeps (0,0) at top-left like the maze

    plt.show()

def plot(iddfs, best, title, ylabel, filename):
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


def plot_mean_times(items, index):

    names = list(items.keys())
    mean_times = [items[name][index] for name in names]

    plt.figure()
    plt.bar(names, mean_times)
    plt.title("BestFS Mean Time by Heuristic", fontsize=16, fontweight="bold")
    plt.ylabel("Mean Time (minutes)")
    plt.xlabel("Heuristic")
    plt.show()


def plot_mean_path_lengths(items, index):

    names = list(items.keys())
    mean_paths = [items[name][index] for name in names]

    plt.figure()
    plt.bar(names, mean_paths)
    plt.title("BestFS Mean Path Length by Heuristic", fontsize=16, fontweight="bold")
    plt.ylabel("Mean Path Length")
    plt.xlabel("Heuristic")
    plt.show()


def plot_variance(items, index):
    names = list(items.keys())
    variances = [items[name][index] for name in names]

    plt.figure()
    plt.bar(names, variances)
    plt.title("BestFS Variance by Heuristic", fontsize=16, fontweight="bold")
    plt.ylabel("Variance")
    plt.xlabel("Heuristic")
    plt.show()
