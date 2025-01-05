import numpy as np

# Monte Carlo Simulation for Risk Assessment
np.random.seed(42)  # For reproducibility

# Simulate 1000 risk scenarios for each project
risk_simulation = {
    project: np.random.normal(loc=risk_mean, scale=0.1, size=1000)
    for project, risk_mean in zip(esg_data["Project"], [0.2, 0.4, 0.4, 0.6, 0.1])  # Mean risk levels
}

# Eg: Calculate average risk for "Solar Farm"
average_risk = np.mean(risk_simulation["Solar Farm"])
print(f"\nAverage Risk for Solar Farm: {average_risk:.2f}")
