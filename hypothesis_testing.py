import numpy as np

# 1. Generate two independent groups
group_a = np.random.normal(loc=55, scale=10, size=100) # Mean 55
group_b = np.random.normal(loc=50, scale=10, size=100) # Mean 50

# 2. Compute basic stats
mean_a, mean_b = sum(group_a)/len(group_a), sum(group_b)/len(group_b)
var_a = sum((x - mean_a)**2 for x in group_a) / len(group_a)
var_b = sum((x - mean_b)**2 for x in group_b) / len(group_b)

# 3. Compute Difference in Means
mean_diff = mean_a - mean_b

# 4. Two-Sample Z-Statistic Calculation
# Formula: (mean_a - mean_b) / sqrt((var_a/n1) + (var_b/n2))
n1, n2 = len(group_a), len(group_b)
pooled_se = ((var_a / n1) + (var_b / n2))**0.5
z_stat = mean_diff / pooled_se

# 5. Interpretation (Alpha = 0.05, Critical Value = 1.96)
if abs(z_stat) > 1.96:
    result = "Reject H0: Significant difference between groups."
else:
    result = "Fail to Reject H0: No significant difference found."

print(f"Difference in Means: {mean_diff:.2f}")
print(f"Z-Statistic: {z_stat:.2f}")
print(f"Conclusion: {result}")
