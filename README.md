# Portfolio Optimization with Quantum Computing

This repository contains a small example using Qiskit to solve a portfolio optimization problem.

## Requirements

- Python 3.11+
- `qiskit`, `qiskit_aer`, `qiskit_finance`, `qiskit_optimization`, and `qiskit_ibm_provider`

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

## GitHub Actions and IBM Quantum

This repository includes a workflow (`ibm-quantum.yml`) that can run the
optimization on IBM Quantum backends. To enable it, add the following secrets
to your repository:

- `IBM_QUANTUM_TOKEN` – your IBM Quantum API token.
- `IBM_QUANTUM_BACKEND` – (optional) name of the backend to use, e.g.
  `ibmq_qasm_simulator`.

Once configured you can trigger the workflow manually from the Actions tab or
whenever the workflow file or script changes.
