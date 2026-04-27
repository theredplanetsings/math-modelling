#!/usr/bin/env python3
"""k-means clustering with k=2 and a Cartesian grid plot.

Data points: (1,1), (2,2), (4,2), (4,4), (5,5)
Initial centroids: (2,2), (5,5)
"""

from math import sqrt
from typing import Dict, List, Sequence, Tuple

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

Point = Tuple[float, float]

def euclidean_distance(a: Point, b: Point) -> float:
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def assign_clusters(points: Sequence[Point], centroids: Sequence[Point]) -> Dict[int, List[Point]]:
    clusters: Dict[int, List[Point]] = {i: [] for i in range(len(centroids))}
    for p in points:
        closest_idx = min(range(len(centroids)), key=lambda i: euclidean_distance(p, centroids[i]))
        clusters[closest_idx].append(p)
    return clusters


def recompute_centroids(clusters: Dict[int, List[Point]], old_centroids: Sequence[Point]) -> List[Point]:
    new_centroids: List[Point] = []
    for i in range(len(old_centroids)):
        pts = clusters[i]
        if not pts:
            new_centroids.append(old_centroids[i])
            continue
        mean_x = sum(p[0] for p in pts) / len(pts)
        mean_y = sum(p[1] for p in pts) / len(pts)
        new_centroids.append((mean_x, mean_y))
    return new_centroids

def kmeans(points: Sequence[Point], initial_centroids: Sequence[Point], max_iter: int = 20):
    centroids = list(initial_centroids)
    for iteration in range(1, max_iter + 1):
        clusters = assign_clusters(points, centroids)
        new_centroids = recompute_centroids(clusters, centroids)

        print(f"Iteration {iteration}")
        for idx, pts in clusters.items():
            print(f"  Cluster {idx + 1}: {pts}")
        print(f"  Centroids: {new_centroids}\n")

        if all(euclidean_distance(centroids[i], new_centroids[i]) < 1e-12 for i in range(len(centroids))):
            return clusters, new_centroids, iteration
        centroids = new_centroids

    return clusters, centroids, max_iter

def plot_clusters(
    points: Sequence[Point],
    clusters: Dict[int, List[Point]],
    initial_centroids: Sequence[Point],
    final_centroids: Sequence[Point],
) -> None:
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

    fig, ax = plt.subplots(figsize=(7, 7))

    # Plot clustered points with circles around each included point.
    for idx, pts in clusters.items():
        color = colors[idx % len(colors)]
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        ax.scatter(xs, ys, s=80, color=color, label=f"Cluster {idx + 1}", zorder=3)

        for p in pts:
            ax.add_patch(Circle(p, radius=0.23, fill=False, edgecolor=color, linewidth=2, zorder=2))
            ax.text(p[0] + 0.06, p[1] + 0.07, f"{p}", fontsize=10)

    # Show initial and final centroids.
    ax.scatter(
        [c[0] for c in initial_centroids],
        [c[1] for c in initial_centroids],
        marker="x",
        s=120,
        linewidths=3,
        color="black",
        label="Initial centroids",
        zorder=4,
    )
    ax.scatter(
        [c[0] for c in final_centroids],
        [c[1] for c in final_centroids],
        marker="P",
        s=110,
        color="crimson",
        label="Final centroids",
        zorder=4,
    )

    # Cartesian grid and axes.
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_xticks(range(0, 7))
    ax.set_yticks(range(0, 7))
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.axhline(0, color="black", linewidth=1.2)
    ax.axvline(0, color="black", linewidth=1.2)
    ax.set_aspect("equal", adjustable="box")

    ax.set_title("k-means Clustering (k=2) for Problem 2")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper left")

    plt.tight_layout()
    plt.show()

def main() -> None:
    points: List[Point] = [(1, 1), (2, 2), (4, 2), (4, 4), (5, 5)]
    initial_centroids: List[Point] = [(1, 1), (4, 4)]

    clusters, final_centroids, iters = kmeans(points, initial_centroids)

    print("Converged summary")
    print(f"  Iterations: {iters}")
    print(f"  Final Cluster 1: {clusters[0]}")
    print(f"  Final Cluster 2: {clusters[1]}")
    print(f"  Final centroids: {final_centroids}")

    plot_clusters(points, clusters, initial_centroids, final_centroids)

if __name__ == "__main__":
    main()