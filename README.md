# heston-abm
# Heston Model with Heterogeneous Agents: Volatility Smile Simulation

## Overview

This project explores whether the volatility smile observed in option markets can emerge endogenously from agent behavior. It combines the Heston stochastic volatility model with an agent-based market, where different types of traders interact dynamically.

The goal is to replicate realistic option pricing behavior by simulating the decisions of fundamental traders, momentum traders, and implied volatility (IV)-based option traders. This hybrid model bridges classical finance theory with behavioral simulation.

## Key Features

* **Stochastic Volatility:** Underlying asset price follows the Heston model
* **Heterogeneous Agents:** Including IV traders, momentum traders, and fundamentalists
* **Option Pricing:** Black-Scholes pricing with implied volatility estimation
* **Volatility Smile Analysis:** Generate and compare IV curves under different scenarios
* **Statistical Testing:** Evaluate hypotheses using t-tests and correlation analysis

## Project Structure

```
project/
├── agents.py           # Definitions of agent types
├── market.py           # Heston process and option pricing
├── model.py            # Core simulation model
├── analysis.py         # Statistical analysis functions
├── visualization.py    # Plotting utilities
├── main.ipynb          # Jupyter notebook to run the simulation
├── README.md           # Project overview and instructions
└── requirements.txt    # Python dependencies
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/heston-abm-smile.git
   cd heston-abm-smile
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the notebook:

   ```bash
   jupyter notebook main.ipynb
   ```

## Example Visuals

* Time series of asset price and variance
* Volatility smiles with and without IV traders
* Statistical test results (t-test, correlation)

## Hypotheses Tested

1. The volatility smile emerges when IV-based traders are present
2. The smile becomes more convex with more momentum traders
3. There is a negative correlation between price and volatility (leverage effect)

