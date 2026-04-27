# Clustering

## Overview
This module introduces unsupervised learning through hierarchical clustering and k-means clustering, with examples ranging from small hand-worked geometric datasets to larger movie-rating and customer-segmentation datasets.

The notebooks and scripts emphasize how similarity measures, distance metrics, and algorithmic update rules produce data-driven groupings without labeled outcomes.

## Files in This Directory

- `tutorial.ipynb`: introductory clustering walkthrough and conceptual setup
- `classExample.ipynb`: in-class style clustering examples on small datasets
- `clusterMovies.ipynb`: clustering workflow using movie metadata and ratings
- `pass_fail_dendrogram.py`: single-link hierarchical clustering demo on final-grade values
- `problem2_kmeans_k2_plot.py`: k-means (k=2) worked example with iterative centroid updates and plotting
- `movies.csv`: movie metadata used in clustering experiments
- `ratings.csv`: user-item ratings data used for movie clustering
- `Wholesale customers data.csv`: customer feature dataset for clustering/segmentation analysis
- `movieClusterHierarchical.txt`: saved hierarchical clustering grouping output for movies
- `movieClusterKmeans.txt`: saved k-means clustering grouping output for movies
- `single_link_dendrogram.png`: generated dendrogram image from `pass_fail_dendrogram.py`

## What Is Being Tested

### 1. Distance-Driven Similarity Modeling
- Defining how observations are compared using Euclidean distance
- Understanding how feature values induce geometric structure in data
- Interpreting why nearby points are likely to share cluster membership

### 2. Hierarchical Clustering Construction
- Building agglomerative cluster trees using linkage rules (single-link focus)
- Reading dendrograms to interpret merge order and separation scale
- Choosing cut levels to convert a hierarchy into flat cluster assignments

### 3. k-means Iterative Optimization
- Initializing centroids and assigning points to nearest centers
- Recomputing centroids as cluster means until convergence
- Evaluating how initialization and k choice affect final partitions

### 4. Applied Clustering Interpretation
- Grouping movies or customers into behaviorally similar segments
- Comparing cluster outputs across hierarchical and partition-based methods
- Connecting computational clusters to meaningful domain narratives

## Notebook and Script Workflow

### Part A: Concept and Class-Scale Examples
- Uses `tutorial.ipynb` and `classExample.ipynb` to introduce clustering goals
- Demonstrates small, interpretable datasets for manual verification
- Establishes intuition for distance, grouping, and cluster boundaries

### Part B: Hierarchical Clustering Demonstration
- Runs `pass_fail_dendrogram.py` on one-dimensional final-grade data
- Produces `single_link_dendrogram.png` for visual merge interpretation
- Reinforces single-link behavior and dendrogram reading

### Part C: k-means Worked Example
- Executes `problem2_kmeans_k2_plot.py` on 2D points with k=2
- Prints per-iteration cluster assignments and updated centroids
- Visualizes initial and final centroids to show convergence behavior

### Part D: Real Dataset Clustering
- Uses `clusterMovies.ipynb` with `movies.csv` and `ratings.csv`
- Stores representative clustering outputs in `movieClusterHierarchical.txt` and `movieClusterKmeans.txt`
- Extends the same methodology to customer-style data in `Wholesale customers data.csv`

## Key Parameters
- `k`: number of clusters used in k-means
- `centroids`: current center points used for assignment and updates
- `max_iter`: iteration cap for k-means convergence loops
- `linkage_matrix`: hierarchical merge structure used to draw dendrograms
- `method='single'`: linkage choice in agglomerative clustering scripts
- `movies.csv`, `ratings.csv`, `Wholesale customers data.csv`: raw data sources used in notebook experiments

## Mathematical Significance
Clustering addresses unsupervised structure discovery: given only feature vectors, the goal is to reveal latent groupings that minimize within-cluster dissimilarity and/or preserve meaningful between-cluster separation.

These examples highlight two foundational paradigms:
- Hierarchical clustering, which builds a nested tree of merges and supports multi-resolution analysis
- k-means clustering, which solves a centroid-based partitioning problem through iterative assignment and update steps

Together, they show how geometric assumptions, optimization strategy, and representation choices shape practical exploratory analysis in applied mathematics and data science.

## Usage
1. Open the notebooks in Jupyter and run cells in order.
2. In `tutorial.ipynb` and `classExample.ipynb`, modify point sets or distances to see how cluster boundaries change.
3. Run `pass_fail_dendrogram.py` to generate and inspect `single_link_dendrogram.png`.
4. Run `problem2_kmeans_k2_plot.py`, then vary initial centroids and compare convergence outcomes.
5. In `clusterMovies.ipynb`, change the number of clusters and contrast hierarchical vs k-means assignments.
6. Explore `Wholesale customers data.csv` with different feature subsets or scaling choices to test segmentation stability.