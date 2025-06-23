# Portfolio Optimization with Quantum Computing

This repository contains a small example using Qiskit to solve a portfolio optimization problem.

## Requirements

- Python 3.11+
- `qiskit`, `qiskit_aer`, `qiskit_finance`, `qiskit_optimization`, and `qiskit-azure-quantum`

To install the dependencies run:

```bash
pip install .
```

## Running

Execute the module with Python:

```bash
python -m quantum_portfolio
```

The example creates a simple portfolio of four assets and uses QAOA to find an optimal allocation given a budget and risk factor.

## GitHub Actions and Azure Quantum

This repository includes a workflow (`azure-quantum.yml`) that can run the
optimization on Azure Quantum backends. To enable it, add the following secrets
to your repository:

- `AZURE_QUANTUM_RESOURCE_ID` – your Azure Quantum workspace resource ID.
- `AZURE_QUANTUM_LOCATION` – the region of the workspace, e.g. `westus`.
- `AZURE_QUANTUM_BACKEND` – (optional) name of the backend to use, e.g.
  `ionq.simulator`.

Once configured you can trigger the workflow manually from the Actions tab or
whenever the workflow file or script changes.
