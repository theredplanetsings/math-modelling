# Bracketology and Colley Rankings

## Overview
This module applies linear algebra and sports analytics to NCAA basketball data using the **Colley rating method**. The core goal is to rank teams from game outcomes and test how different weighting choices affect rankings and predictive behavior.

The exercises move from a baseline unweighted model to custom weighted variants, then use those ratings for tournament-style matchup predictions.

## Files in This Directory

- `colleyWeightedRanking.ipynb`: Main notebook implementing the ranking and prediction workflow
- `NCAA_2008_Games.txt`, `NCAA_2008_Teams.txt`: 2007-08 season game/team data
- `NCAA_2007_Games.txt`, `NCAA_2007_Teams.txt`: 2006-07 season game/team data

Data format follows the Massey ratings convention (team IDs, scores, home/away/neutral flags, and game dates).

## What Is Being Tested

### 1. Colley System Construction
- Building the Colley matrix \(C\) and right-hand side vector \(b\) from win/loss game data
- Solving the linear system \(Cr=b\) to obtain team ratings
- Verifying matrix updates from pairwise game interactions

### 2. Weighting Strategy Effects
- Comparing **uniform weighting** (all games weighted equally) against **custom weighting**
- Testing location-sensitive game values (home/away/neutral win multipliers)
- Testing time-sensitive weighting (later-season games weighted more heavily)
- Observing how ranking order changes under alternate assumptions

### 3. Predictive Utility
- Computing in-sample predictability: percentage of games where higher Colley rating matches game winner
- Using rankings as a simple decision rule for head-to-head predictions

### 4. Bracket Simulation Logic
- Mapping tournament team names to dataset naming conventions
- Simulating round-by-round advancement using rating comparisons only
- Producing region champions, Final Four picks, and championship pick from the model

## Notebook Workflow

### Part A: Baseline Colley Ranking (2008)
- Loads 2008 team/game files
- Builds an unweighted (or optionally weighted) Colley system
- Prints top-\(k\) ranked teams
- Reports model predictability on the season data

### Part B: 2008 Bracket Prediction
- Uses 2008 Colley ratings to pick winners in a full NCAA bracket structure
- Advances winners through rounds deterministically by rating

### Part C: 2006-07 Pre-Tournament Ranking (Uniform)
- Filters 2007 season games to **pre-March Madness** only
- Ranks all Division I teams with uniform weights

### Part D: 2006-07 Pre-Tournament Ranking (Custom Weights)
- Applies a custom time ramp and location multipliers
- Compares resulting top teams against the uniform baseline

## Key Parameters
- `k`: number of top teams displayed (`0` means all teams)
- `useWeighting`: toggle for weighted vs uniform game treatment
- `segmentWeighting`: piecewise season weighting schedule
- `m1`, `m2`: linear early-to-late season weight bounds
- `weight_home_win`, `weight_away_win`, `weight_neutral_win`: location multipliers

## Mathematical Significance
Colley rankings model schedule outcomes as a linear system where each game contributes coupled constraints between teams. This provides a reproducible and interpretable alternative to poll-based rankings.

The experiments illustrate a common modeling tradeoff:
- **Stability and simplicity** from uniform assumptions
- **Potential realism gains** from context-aware weighting (time and location)

In bracketology terms, the notebook tests whether a mathematically consistent rating system can serve as a practical baseline for tournament forecasting.

## Usage
1. Open `colleyWeightedRanking.ipynb` in Jupyter.
2. Run cells in order.
3. Change weighting parameters and rerun ranking sections.
4. Compare top-team lists and predictability across weighting choices.
5. Re-run bracket simulation to see how picks shift with rating changes.