# Mathematical Modelling

This repo will contain coursework, projects, and implementations relevant to applied mathematical modelling methods. It will serve as a collection of computational techniques & simulations used for modelling real-world phenomena with mathematical frameworks.

Following along with MAT-210 - Mathematical Modelling at Davidson College, Spring 2026

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
│   └── README.md         # project docs
├── README.md             # self-explanatory
└── LICENSE
```

## Contents as of 02/06/2026:

### Project 1 - Central Limit Theorem Simulation
**Directory:** `1_Central-Limit-Theorem/`

Monte Carlo simulation demonstrating the Central Limit Theorem through dice rolling experiments. Explores how sample averages converge to a normal distribution with both uniform and non-uniform probability distributions.

### Project 2 - Monte Carlo Simulations
**Directory:** `2_Monte-Carlo/`

Collection of Monte Carlo simulation techniques applied to various problems:
- **Buffon's Needle:** Estimating π using geometric probability
- **Fish Tank Simulations:** Probabilistic modeling scenarios
- **Scam School Problem:** Monte Carlo approach to probability puzzles

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