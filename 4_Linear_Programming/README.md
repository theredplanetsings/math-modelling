# Linear Programming and Optimization

## Overview
Linear programming (LP) is a mathematical optimization technique for maximizing or minimizing a linear objective function subject to linear constraints. LP provides a rigorous framework for resource allocation decisions under competing constraints—finding the "best" solution when multiple goals conflict and resources are limited.

The fundamental structure of an LP problem:
```
Maximize (or Minimize):  c₁x₁ + c₂x₂ + ... + cₙxₙ    (objective function)

Subject to:  a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ  ≤  b₁
             a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ  ≤  b₂
             ...                                        (constraints)
             x₁, x₂, ..., xₙ ≥ 0                      (non-negativity)
```

**Extensions**:
- **Integer Programming (IP)**: Variables must take integer values (indivisible resources)
- **Mixed-Integer Programming (MIP)**: Some variables are integers, others continuous

## Problem Types

This directory contains three classic optimization problems demonstrating different LP concepts:

### 1. Resource Allocation (`LP_Problems.pdf` Problem 1)
**Life Vests and Life Boats** - A 2-variable problem exploring volume and capacity trade-offs.

- Optimize the mix of safety equipment to maximize capacity within volume constraints
- Solved using **graphical method** (plotting feasible region, finding optimal vertex)
- Demonstrates **integer programming** (discrete units) vs. continuous relaxation
- Includes **sensitivity analysis** showing how parameter changes affect solutions

### 2. Production Planning (`LP_Problems.pdf` Problem 2)
**Manufacturing Product Mix** - A 3-variable problem with multiple machine constraints.

- Determine production levels for three products to maximize profit
- Each product requires different machine hours on three machines (mailing, lathe, grinder)
- Identifies **binding constraints** (bottleneck resources at full capacity)
- Illustrates **shadow prices** (marginal value of additional resources)

### 3. Time and Budget Optimization (`LP_Problems.pdf` Problem 3)
**Mariko's Class Scheduling** - A mixed-integer programming problem.

- Maximize classes taken while satisfying work-hour and budget constraints
- Classes come in fixed 5-hour increments (integer constraint)
- Work hours are continuous (fractional hours allowed)
- Demonstrates **mixed-integer programming** and non-unique solutions

## Directory Contents

- **`LP_Problems.pdf`**: Original problem statements
- **`LP_Solutions.pdf`**: Handwritten solutions including graphical methods, algebraic derivations, and interpretations
- **`1e.xlsx`** + **`1e report.mp4`**: Excel implementation of Problem 1 using SimplexLP solver
- **`2b.xlsx`** + **`2b report.mp4`**: Excel implementation of Problem 2 using SimplexLP solver
- Video files show solver execution since SimplexLP doesn't produce downloadable reports

## Solution Methods

### Graphical Method (2 Variables)
1. Plot all constraints on the x₁-x₂ plane
2. Identify the **feasible region** (area satisfying all constraints)
3. Draw contour lines of the objective function
4. Find the optimal corner point (vertex of feasible region)

**Why it works**: The feasible region is a convex polygon; the optimum always occurs at a vertex.

### Simplex Algorithm (General Case)
- Systematically traverses vertices of the feasible region
- Moves from vertex to vertex, improving the objective function
- Terminates at optimal vertex (or determines unboundedness/infeasibility)
- Used by SimplexLP solver for Excel-based solutions

### Integer Programming
- Enumerate integer points within feasible region
- Or use **branch-and-bound** algorithms for larger problems
- LP relaxation (ignoring integrality) provides an upper bound on the optimal value

## Mathematical Significance

### Key Concepts
- **Feasible Region**: Set of all points satisfying all constraints (a convex polytope)
- **Optimal Solution**: Vertex of the feasible region maximizing/minimizing the objective
- **Binding Constraints**: Constraints that are exactly satisfied (active) at the optimum
- **Shadow Price**: How much the objective would improve if a constraint were relaxed by one unit
- **Sensitivity Analysis**: Study of how optimal solution changes with parameter perturbations

### Theoretical Foundation
- **Fundamental Theorem**: If an optimal solution exists and is bounded, it occurs at a vertex
- **Duality**: Every LP has a dual problem; strong duality says optimal values are equal
- **Computational Complexity**: LP is solvable in polynomial time; IP is NP-hard

### Real-World Applications
Linear programming is foundational in operations research and optimization:

- **Manufacturing**: Production scheduling, capacity planning, workforce allocation
- **Supply Chain**: Transportation routes, warehouse location, inventory management
- **Finance**: Portfolio optimization, asset allocation, risk management
- **Energy**: Power grid optimization, fuel blending, renewable integration
- **Agriculture**: Crop planning, fertilizer allocation, harvest scheduling
- **Telecommunications**: Network routing, bandwidth allocation

## Usage

### Excel/SimplexLP Solutions
The Excel files demonstrate LP formulation and solution using SimplexLP:

1. Set up decision variables, objective function, and constraints in spreadsheet format
2. Use SimplexLP solver (Google Sheets OpenSolver add-on) to find optimal solution
3. Generate solution reports showing optimal values, constraint status, and shadow prices
4. Video recordings (`.mp4` files) document solver execution

### Suggested Experiments
- **Problem 1**: Change volume constraints or boat capacity to see feasibility boundaries
- **Problem 2**: Add a fourth product or change profit margins
- **Problem 3**: Increase hourly wage and observe impact on feasible class count
- **General**: Add minimum production requirements or modify constraint parameters

## Key Insight
Linear programming transforms qualitative resource allocation questions into rigorous mathematical frameworks with provably optimal solutions. Constraints model real-world limitations as algebraic inequalities, enabling systematic decision-making under scarcity. The graphical method (2D) and Simplex algorithm (general) both embody the same principle: **optimization means finding the "best corner" of a multi-dimensional feasible region**.