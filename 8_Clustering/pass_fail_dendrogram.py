import matplotlib.pyplot as plt
from pathlib import Path
from scipy.cluster.hierarchy import dendrogram, linkage

# Final grades for the course
grades = [52, 68, 69, 71, 98]
labels = [str(grade) for grade in grades]

# Single-link hierarchical clustering on the one-dimensional grade values
linkage_matrix = linkage([[grade] for grade in grades], method="single", metric="euclidean")

plt.figure(figsize=(8, 4.5))
dendrogram(linkage_matrix, labels=labels, color_threshold=0)
plt.title("Single-Link Hierarchical Clustering Dendrogram")
plt.xlabel("Final grade")
plt.ylabel("Distance")
plt.tight_layout()

output_path = Path(__file__).with_name("single_link_dendrogram.png")
plt.savefig(output_path, dpi=200, bbox_inches="tight")
plt.show()