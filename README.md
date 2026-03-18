# Mathematical Modelling

This repo will contain coursework, projects, and implementations relevant to applied mathematical modelling methods. It will serve as a collection of computational techniques & simulations used for modelling real-world phenomena with mathematical frameworks.

Following with MAT-210 - Mathematical Modelling at Davidson College, Spring 2026

## Repository Structure

```
math-modelling/
├── 1_Central-Limit-Theorem/
│   ├── h1.ipynb          # Central Limit Theorem simulations
│   └── README.md         # Project docs
├── 2_Monte-Carlo/
│   ├── buffon.ipynb      # Buffon's Needle simulation
│   ├── fishtankmc1.ipynb # Fish tank Monte Carlo simulation (part 1)
│   ├── fishtankmc2.ipynb # Fish tank Monte Carlo simulation (part 2)
│   ├── scamSchool.ipynb  # Scam School problem simulation 
│   └── README.md         # Project docs
├── 3_Poisson_Processes/
│   ├── pharmacy.ipynb    # Queuing theory simulation
│   └── README.md         # Project docs
├── 4_Linear_Programming/
│   ├── 1e.xlsx           # Problem 1 Excel solution
│   ├── 1e report.mp4     # SimplexLP solver execution
│   ├── 2b.xlsx           # Problem 2 Excel solution
│   ├── 2b report.mp4     # SimplexLP solver execution
│   ├── LP_Problems.pdf   # Problem statements
│   ├── LP_Solutions.pdf  # Handwritten solutions
│   └── README.md         # Project docs
├── 5_Bracketology/
│   ├── colleyWeightedRanking.ipynb # Colley ranking and bracket predictions
│   ├── NCAA_2007_Games.txt         # 2006-07 game results
│   ├── NCAA_2007_Teams.txt         # 2006-07 team names
│   ├── NCAA_2008_Games.txt         # 2007-08 game results
│   ├── NCAA_2008_Teams.txt         # 2007-08 team names
│   └── README.md                   # Project docs
├── README.md             # self-explanatory
└── LICENSE
```

## Contents as of 03/18/2026:

### Project 1 - Central Limit Theorem Simulation
**Directory:** `1_Central-Limit-Theorem/`

Monte Carlo simulation demonstrating the Central Limit Theorem through dice rolling experiments. Explores how sample averages converge to a normal distribution with both uniform and non-uniform probability distributions.

### Project 2 - Monte Carlo Simulations
**Directory:** `2_Monte-Carlo/`

Collection of Monte Carlo simulation techniques applied to various problems:
- **Buffon's Needle:** Estimating π using geometric probability
- **Fish Tank Simulations:** Probabilistic modeling scenarios
- **Scam School Problem:** Monte Carlo approach to probability puzzles

### Project 3 - Poisson Processes & Queuing Theory
**Directory:** `3_Poisson_Processes/`

Stochastic modeling of queuing systems with real-world applications:
- **Pharmacy Simulation:** Models customer arrivals and service times at a pharmacy using Poisson processes and normal distributions. Simulates an 8-hour business day to determine wait times and closing time delays.

### Project 4 - Linear Programming & Optimisation
**Directory:** `4_Linear_Programming/`

Optimisation techniques for resource allocation under constraints:
- **Life Vests & Boats:** 2-variable resource allocation with graphical method and integer programming
- **Manufacturing Mix:** 3-variable production planning with machine capacity constraints
- **Class Scheduling:** Mixed-integer programming for time and budget optimization
- Solutions implemented using SimplexLP solver in Google Sheets

### Project 5 - Bracketology & Colley Rankings
**Directory:** `5_Bracketology/`

Linear-algebra-based team ranking and tournament forecasting:
- **Colley Rating Method:** Builds and solves a linear system from game outcomes to rank teams
- **Weighting Experiments:** Compares uniform weighting against custom time/location game weights
- **Predictability Testing:** Measures how often rating order matches observed game winners
- **Bracket Simulation:** Uses ratings to generate round-by-round NCAA tournament picks

## Getting Started

Each project directory contains its own README with specific objectives, methodology, and usage instructions. Projects are self-contained and can be explored independently.

**General Requirements:**
- Python 3.8 or higher
- Jupyter Notebook
- Standard scientific Python stack:
  - NumPy
  - Matplotlib
  - Statistics (standard library)
  - Additional requirements listed in individual project directories

**Running the Notebooks:**
1. Clone this repository
2. Navigate to the desired project directory
3. Launch Jupyter Notebook: `jupyter notebook`
4. Open and run the `.ipynb` files sequentially

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.