# Integer Programming

## Overview
This module introduces integer programming through three optimization examples solved with Gurobi: a production planning model, a guard-placement puzzle, and a Sudoku formulation.

The notebooks emphasize how discrete decision variables, linear constraints, and objective functions are combined to represent real-world allocation and feasibility problems that require whole-number solutions.

## Files in This Directory

- `tableChairIP.ipynb`: integer production-planning model for tables and chairs
- `castleIP.ipynb`: integer optimization model for the castle guard-placement puzzle
- `sudokuNotebook.ipynb`: binary integer programming formulation for Sudoku
- `castle.lp`: LP export of the castle model
- `sudoku.lp`: LP export of the Sudoku model
- `sudoku.txt`: puzzle input grid used by the Sudoku notebook

## What Is Being Tested

### 1. Integer and Binary Decision Modeling
- Defining integer decision variables for count-based choices
- Using binary indicator variables for one-of-many assignments
- Enforcing discrete feasibility where fractional solutions are invalid

### 2. Constraint System Design
- Translating problem rules into linear equalities and inequalities
- Encoding resource limits, structural relationships, and assignment logic
- Verifying that constraints fully capture the intended problem statement

### 3. Objective Function Formulation
- Building optimization targets for maximization and feasibility-driven tasks
- Interpreting how objective choice affects selected solutions
- Connecting mathematical objective expressions to practical goals

### 4. Solver-Based Analysis and Validation
- Solving IP/BILP models with Gurobi and interpreting solver output
- Exporting models to `.lp` format for transparency and inspection
- Comparing model expectations with computed optimal or feasible solutions

## Notebook Workflow

### Part A: Table and Chair Integer Production Model
- Creates integer variables for numbers of tables and chairs
- Applies production/resource constraints from the class example
- Solves for an optimal integer production plan

### Part B: Castle Guard-Placement Puzzle
- Defines integer guard variables at castle positions
- Enforces wall-coverage and total-guard constraints
- Maximizes guards on selected strategic positions

### Part C: Sudoku as a Binary Integer Program
- Reads an input puzzle from `sudoku.txt`
- Builds binary variables indicating whether digit $k$ is placed in cell $(i,j)$
- Enforces row, column, subgrid, and clue-consistency constraints
- Solves the puzzle and optionally writes the algebraic model to `sudoku.lp`

## Key Parameters
- `tables`, `chairs`: integer decision variables in the production model
- `guards[i]`: integer guard allocation variables in the castle model
- `G[i,j,k]`: binary Sudoku variable for digit-placement decisions
- `sudoku.txt`: external puzzle specification used to initialize fixed entries
- `model.write('*.lp')`: export step for inspecting generated optimization models

## Mathematical Significance
Integer programming extends linear programming by requiring some or all variables to take discrete values.

These examples show three common modeling patterns:
- General integer optimization for count decisions (production and guard allocation)
- Binary assignment structure for combinatorial feasibility (Sudoku)
- Constraint-driven solution design where correctness and optimality are both essential

Together, they illustrate how optimization translates domain rules into solvable mathematical systems and how modern solvers support practical decision-making in applied mathematics.

## Usage
1. Open each notebook in Jupyter.
2. Run cells in order.
3. In `tableChairIP.ipynb`, modify coefficients or constraints and observe how the optimal integer mix changes.
4. In `castleIP.ipynb`, vary wall or guard constraints to test alternate deployment scenarios.
5. In `sudokuNotebook.ipynb`, replace `sudoku.txt` with a different puzzle and compare solver behavior.
6. Inspect `castle.lp` and `sudoku.lp` to see the generated algebraic model structure.