# Central Limit Theorem Simulation

## Overview
- Monte Carlo simulation demonstrating the Central Limit Theorem through repeated dice rolling experiments
- Shows how sample means converge to a normal distribution as sample size increases, regardless of the underlying distribution

## Notebook Structure

### Part A: Fair Die (Uniform Distribution)
- **Probability**: Equal probability (1/6) for each outcome
- **Sample size**: 100 rolls per experiment
- **Demonstrates**: CLT with uniform distribution and large sample size

### Part B: Fair Die (Small Sample)
- **Probability**: Equal probability (1/6) for each outcome  
- **Sample size**: 1 roll per experiment
- **Demonstrates**: Distribution of individual rolls (no averaging effect)

### Part C: Weighted Die (Non-Uniform Distribution)
- **Probability**: `(4/24, 1/12, 1/24, 1/24, 1/24, 15/24)` - heavily weighted toward 6
- **Sample sizes**: 3, 10, and 100 rolls per experiment
- **Demonstrates**: CLT convergence with increasing sample size, even for skewed distributions

## Key Params
- `number_of_experiments`: Number of independent trials (default: 300)
- `number_of_rolls`: Sample size for each experiment
- `prob`: Probability distribution tuple for die faces

## Usage
Run each section sequentially to observe:
1. How the probability distribution visualizes
2. How sample averages distribute across experiments
3. The progressive normalization effect as sample size increases

## Mathematical Significance
Illustrates that regardless of the parent distribution's shape, the distribution of sample means approaches normality as sample size grows—a fundamental result in statistical theory with broad applications in modeling, inference, and uncertainty quantification