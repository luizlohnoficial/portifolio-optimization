import numpy as np
from qiskit_finance.applications.optimization import PortfolioOptimization
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit.primitives import Sampler


def main():
    # expected returns for four assets
    mu = [0.12, 0.1, 0.07, 0.03]
    # covariance matrix representing risk
    sigma = 0.5 * np.array([
        [0.005, -0.010, 0.004, -0.002],
        [-0.010, 0.040, -0.002, 0.004],
        [0.004, -0.002, 0.023, 0.002],
        [-0.002, 0.004, 0.002, 0.018],
    ])

    risk_factor = 0.5
    budget = 2

    # create quadratic program for portfolio optimization
    portfolio = PortfolioOptimization(expected_returns=mu,
                                      covariances=sigma,
                                      risk_factor=risk_factor,
                                      budget=budget)
    qp = portfolio.to_quadratic_program()

    # solve using QAOA
    sampler = Sampler()
    qaoa = QAOA(sampler)
    optimizer = MinimumEigenOptimizer(qaoa)
    result = optimizer.solve(qp)

    print(result)


if __name__ == "__main__":
    main()
