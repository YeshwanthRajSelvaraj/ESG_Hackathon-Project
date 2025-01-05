import pandas as pd

# Sample ESG Data (can be replaced with real data from APIs or databases)
data = {
    "Project": ["Solar Farm", "Wind Turbine", "Biofuel Plant", "Eco Housing", "Green Data Center"],
    "Environmental": [85, 90, 75, 70, 95],
    "Social": [80, 85, 70, 65, 90],
    "Governance": [88, 86, 80, 75, 92],
    "Cost (M)": [3, 2, 2, 4, 5],
    "Risk Level": ["Low", "Medium", "Medium", "High", "Low"]
}

# Create a DataFrame
esg_data = pd.DataFrame(data)

# Compute overall ESG score (Weighted Average)
esg_data["ESG Score"] = (esg_data["Environmental"] * 0.4 +
                         esg_data["Social"] * 0.3 +
                         esg_data["Governance"] * 0.3)

# Display the ESG Data
print("ESG Data:")
print(esg_data)
