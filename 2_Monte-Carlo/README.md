# Monte Carlo Simulations

## Overview
Collection of Monte Carlo simulation techniques applied to classical probability problems and real-world scenarios. Demonstrates how repeated random sampling can estimate solutions to deterministic problems and model stochastic processes.

## Notebooks

### 1. Buffon's Needle (`buffon.ipynb`)
**Classic geometric probability experiment for estimating π**

- **Problem**: A needle of length L is randomly dropped on a floor with parallel lines separated by distance D
- **Parameter Configurations Tested**:
  - L = D = 1 (standard case, needle length equals line spacing)
  - L = 1/2, D = 2 (needle shorter than spacing)
  - L = 1, D = 20 (very wide spacing)
  - L = 3, D = 4 (Fox's historical experiment)
- **Method**: Simulates random drops and counts crossings to estimate π using the formula: π ≈ 2nL/(Dc) where n = drops, c = crossings
- **Key Variables**:
  - `n`: Number of needle drops (default: 5000; 530 for Fox's experiment)
  - `verticalPosition`: Random y-coordinate of needle center
  - `theta`: Random angle of needle orientation
- **Fox's Experiment Analysis**: Runs 100,000 simulations of 530 tosses to assess the probability of achieving Fox's remarkably accurate 1901 result (π ≈ 3.1423)
- **Demonstrates**: Convergence of Monte Carlo estimate with increasing trials; elegant connection between geometry and probability; sensitivity to parameter choices; statistical validation of historical results

### 2. Fish Tank Modeling - Part 1 (`fishtankmc1.ipynb`)
**Introductory inventory management simulation**

- **Scenario**: Pet store stocking fish tanks with random customer arrivals
- **Parameters**:
  - `a = 1/3`: Daily probability of customer arrival
  - `days_for_delivery = 2`: Lead time for tank orders
  - `stock = 1`: Initial inventory
- **Simulation**: 3-week period tracking daily inventory, sales, and lost customers
- **Output**: Day-by-day trace of stock levels, customer arrivals, sales, and missed opportunities
- **Demonstrates**: Basic Monte Carlo framework for stochastic inventory systems; first-pass exploration of ordering strategies

### 3. Fish Tank Modeling - Part 2 (`fishtankmc2.ipynb`)
**Advanced inventory optimization with profit analysis**

- **Enhancements over Part 1**:
  - `number_simulations = 1000`: Multiple independent 2-year scenarios
  - Profit/loss accounting system
  - Multiple ordering strategies (order-when-out vs. fixed-interval)
  - Overstock cost tracking
- **Economic Parameters**:
  - `saleprofit = $20`: Revenue per tank sold
  - `lostloss = $10`: Opportunity cost per lost customer
  - `overstockloss = $0.10`: Nightly holding cost per excess tank
- **Parameters to Explore**:
  - `a = 1/7`: Customer arrival probability
  - `days_for_delivery = 5`: Order lead time
  - `fixed_delivery = 7`: Standing order interval (0 to disable)
  - `order_when_out`: Reorder policy flag
- **Outputs**: 
  - Profit distribution across simulations
  - Average profit and standard deviation
  - Histogram visualization
  - Detailed logs saved to `fishtankmc2-output.txt`
- **Demonstrates**: Monte Carlo for optimization; sensitivity analysis; statistical distribution of outcomes under uncertainty

### 4. Scam School Card Trick (`scamSchool.ipynb`)
**Probability analysis of card adjacency problem**

- **Problem**: From a shuffled standard deck, two random card values (ace through king) are selected. What's the probability they appear adjacent in the deck?
- **Origin**: May 2009 episode of Internet show _Scam School_ (host Brian Brushwood) claiming approximately 70% probability
- **Method**: 
  - Simulate random deck permutation
  - Select two random card values
  - Check if any instance of these values sits side-by-side
  - Extended simulation: 100,000 trials to empirically verify the claim
- **Result**: Simulation confirms probability of ~70%, validating Brushwood's claim
- **Key Insight**: With 4 cards of each value in a 52-card deck, multiple opportunities for adjacency increase probability beyond naive expectation
- **Demonstrates**: Monte Carlo verification of counterintuitive probability claims; usefulness of simulation for complex combinatorics; empirical validation over analytical calculation

## Common Patterns
All notebooks employ the Monte Carlo method:
1. **Define the problem** with probabilistic or geometric parameters
2. **Generate random inputs** (angles, arrivals, permutations)
3. **Simulate the process** many times
4. **Aggregate results** to estimate probabilities, expected values, or optimal strategies

## Usage
Each notebook is self-contained and can be run independently:
1. Open the notebook in Jupyter
2. Execute cells sequentially
3. Modify parameters to explore different scenarios
4. Observe convergence and variability in results

## Mathematical Significance
Monte Carlo methods transform intractable analytical problems into computational experiments. These simulations illustrate:
- **Buffon's Needle**: Geometric probability and numerical integration
- **Fish Tank Models**: Stochastic operations research and decision-making under uncertainty
- **Scam School**: Empirical validation of probability in complex sample spaces

The power of Monte Carlo lies in its generality—applicable to any system that can be modeled with random processes, from physics and finance to logistics and game theory.