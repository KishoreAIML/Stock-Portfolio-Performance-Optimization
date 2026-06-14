import numpy as np
from scipy.optimize import minimize

def optimize_portfolio(expected_returns, cov_matrix, constraints=None, risk_free_rate=0.0):
    
    num_assets = len(expected_returns)

    initial_weights = np.array([1.0 / num_assets] * num_assets)

    def objective_function(weights):
        portfolio_return = np.sum(expected_returns * weights)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
        return -sharpe_ratio 

    
    bounds = [(0, 1) for _ in range(num_assets)]

    
    result = minimize(
        objective_function,
        initial_weights,
        method='SLSQP',
        bounds=bounds
    )


    optimized_weights = result.x

    portfolio_return = np.sum(expected_returns * optimized_weights)
    portfolio_volatility = np.sqrt(np.dot(optimized_weights.T, np.dot(cov_matrix, optimized_weights)))

    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

    optimization_results = {
        "Portfolio Weights": optimized_weights,
        "Portfolio Return": portfolio_return,
        "Portfolio Volatility": portfolio_volatility,
        "Sharpe Ratio": sharpe_ratio,
    }

    return optimization_results