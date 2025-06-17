# Portfolio Optimization with Quantum Computing

This repository contains a small example using Qiskit to solve a portfolio optimization problem.

## Requirements

- Python 3.11+
- `qiskit`, `qiskit_aer`, `qiskit_finance`, and `qiskit_optimization`

To install the dependencies run:

```bash
pip install qiskit qiskit_aer qiskit_finance qiskit_optimization
```

## Running

Execute the script with Python:

```bash
python quantum_portfolio.py
```

The example creates a simple portfolio of four assets and uses QAOA to find an optimal allocation given a budget and risk factor.
