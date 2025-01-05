from pulp import *

prob = LpProblem("Green_Finance_Optimization", LpMaximize)

decision_vars = [LpVariable(f"x{i}", cat="Binary") for i in range(len(esg_data))]

prob += lpSum([decision_vars[i] * esg_data["ESG Score"][i] for i in range(len(esg_data))])

budget = 10
prob += lpSum([decision_vars[i] * esg_data["Cost (M)"][i] for i in range(len(esg_data))]) <= budget

prob.solve()

print("\nSelected Projects for Investment:")
for i, var in enumerate(decision_vars):
    if var.value() == 1:
        print(f"- {esg_data['Project'][i]}")
