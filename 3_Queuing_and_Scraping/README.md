# Queuing Theory and Web Scraping

## Overview
Stochastic modeling of queuing systems using probability theory and discrete event simulation. Demonstrates how random arrival processes and service distributions interact to create wait times, bottlenecks, and operational inefficiencies in real-world service systems.

## Notebooks

### 1. Pharmacy Simulation (`pharmacy.ipynb`)
**Single-server queue model with Poisson arrivals and normal service times**

- **Problem**: A pharmacy operates from 9:00 AM to 5:00 PM and accepts prescriptions until closing. How late must the pharmacist stay to complete all prescriptions received during business hours?
- **Model Source**: Based on S. M. Ross, _A Course in Simulation_
- **System Parameters**:
  - `minutes_in_day = 480`: Operating hours (8-hour day)
  - `a = 32/480`: Average arrival rate (32 customers expected per day)
  - `ncust = 200`: Upper bound for customer array initialization
- **Stochastic Components**:
  - **Arrival Process**: Poisson process with exponential inter-arrival times
    - Inter-arrival times: `iat = -1/a * log(r)` where r ~ Uniform(0,1)
    - Only customers arriving before 5:00 PM are accepted
  - **Service Process**: Normal distribution
    - Mean service time: 10 minutes
    - Standard deviation: 4 minutes
    - `st = 10 + 4 * randn(ncust)`
- **Key Variables**:
  - `at`: Arrival time of each prescription (cumulative)
  - `st`: Service time required for each prescription
  - `ft`: Finish time after waiting in queue and being served
- **Queue Dynamics**:
  - First customer: `ft[0] = at[0] + st[0]` (no wait)
  - Subsequent customers: `ft[i] = max(at[i] + st[i], ft[i-1] + st[i])`
    - Uses arrival time + service if no queue
    - Uses previous finish time + service if waiting
- **Outputs**:
  - Finish time of last prescription
  - Minutes past 5:00 PM the pharmacist must stay
  - Implicit: total wait time distribution across all customers
- **Demonstrates**: 
  - Single-server queuing theory (M/G/1 queue variant)
  - Poisson process generation via exponential inter-arrival times
  - Queue formation from stochastic arrival/service mismatch
  - Real-world operational scheduling challenges

### Programming Notes Section
The notebook includes instructional material on NumPy array operations:
- Generating uniform random numbers with `np.random.rand()`
- Finding array indices meeting conditions with `np.argwhere()` vs. `np.where()`
- Practical differences for array subsetting and length calculations
- Demonstrates why `np.where()` is preferred for creating filtered subarrays

## Common Patterns
Queuing simulations follow a discrete event simulation framework:
1. **Generate arrival times** using a random process (Poisson/exponential)
2. **Generate service requirements** using a probability distribution
3. **Process events chronologically**, tracking system state (queue length, server status)
4. **Compute performance metrics** (wait times, utilization, overtime)

## Usage
The pharmacy notebook can be run as-is:
1. Open `pharmacy.ipynb` in Jupyter
2. Execute cells sequentially
3. Observe a single-day simulation with randomized arrivals and service times
4. Re-run to see variability in outcomes (different random seeds)

**Suggested Experiments**:
- Increase arrival rate `a` to create congestion
- Change service time distribution parameters (mean/std)
- Simulate multiple days to analyze distribution of closing times
- Add a second pharmacist (multiple server model)
- Implement a maximum queue length (customer balking)

## Mathematical Significance
Queuing theory provides analytical and computational tools for understanding service systems:

- **Pharmacy Model**: An M/G/1 queue (Markovian arrivals, General service distribution, 1 server) where:
  - Arrivals follow a Poisson process (memoryless, exponentially distributed inter-arrivals)
  - Service times are normally distributed (more realistic than exponential)
  - Queue discipline is FIFO (first in, first out)

- **Real-World Applications**:
  - Healthcare: Emergency room staffing, appointment scheduling
  - Retail: Checkout lane optimization
  - Call Centers: Agent allocation and service level agreements
  - Manufacturing: Production line bottleneck analysis

- **Key Insight**: Even when average service rate exceeds average arrival rate, queues form due to randomness. The pharmacist stays late not because of insufficient capacity, but because of arrival/service variability and the constraint that customers arriving before 5:00 must be served.

The simulation approach is essential when analytical solutions are intractable (e.g., non-exponential service distributions, time-varying arrival rates). Monte Carlo simulation estimates the distribution of outcomes rather than just expected values, revealing operational risks and variability.