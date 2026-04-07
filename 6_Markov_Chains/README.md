# Markov Chains

## Overview
This module introduces discrete-time Markov chain modeling through two examples: customer switching behavior between competing businesses and state transitions in a board game.

The notebooks emphasize how transition probabilities define long-run behavior, how matrix powers evolve state distributions over time, and how Monte Carlo simulation can approximate theoretical Markov outcomes.

## Files in This Directory

- `cleanersSimulation.ipynb`: Monte Carlo simulation of two-state customer switching between dry cleaners
- `cherryO.ipynb`: Markov chain transition-matrix analysis of Hi Ho Cherry-O

## What Is Being Tested

### 1. State-Based Modeling
- Defining states that represent system conditions (business choice or game status)
- Representing one-step movement between states with fixed transition probabilities
- Interpreting state updates as a stochastic process over repeated time steps

### 2. Transition Matrix Construction
- Building a transition matrix from model assumptions
- Using matrix entries to encode movement likelihood between states
- Checking how reachable states emerge over multiple steps

### 3. Time Evolution and Long-Run Behavior
- Evolving an initial state vector through repeated transitions
- Using matrix powers to evaluate multi-step behavior
- Observing when target states become possible and how mass shifts across states

### 4. Simulation vs Analytical Perspective
- Running many random trials to estimate state frequencies over time
- Comparing empirical simulation trends with Markov chain expectations
- Reinforcing the relationship between probabilistic simulation and linear algebraic analysis

## Notebook Workflow

### Part A: Cleaners Customer Switching Simulation
- Initializes a two-state model for customer choice between Spotless and Starch
- Runs many simulations across fixed time periods
- Records state counts by time step to observe convergence trends

### Part B: Hi Ho Cherry-O Transition Matrix Analysis
- Constructs an 11-state transition matrix for game progress
- Defines an initial state vector
- Applies matrix powers to determine when completion states become nonzero

## Key Parameters
- `num_experiments`: number of simulation trials in the cleaners model
- `time_periods`: number of steps per simulation run
- `initial_state`: starting state for each simulation
- `G`: transition matrix for the Hi Ho Cherry-O Markov chain
- `firstTurn`: initial state vector for matrix-power analysis

## Mathematical Significance
Markov chains provide a compact framework for modeling systems where the next state depends only on the current state and fixed transition rules.

These examples connect two complementary approaches:
- Monte Carlo estimation for empirical behavior over many random runs
- Matrix-based analysis for exact multi-step state evolution

Together, they illustrate how probabilistic modeling and linear algebra support practical forecasting and interpretation in applied math settings.

## Usage
1. Open each notebook in Jupyter.
2. Run cells in order.
3. In `cleanersSimulation.ipynb`, vary transition probabilities, simulation count, or initial state and compare trajectories.
4. In `cherryO.ipynb`, vary matrix powers or initial conditions to examine reachability and progression.
5. Compare simulation-based and matrix-based insights across both notebooks.