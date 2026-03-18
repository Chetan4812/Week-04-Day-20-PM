import numpy as np
import matplotlib.pyplot as plt

# Generate dataset (size=1000) from Normal Distribution
data = np.random.normal(loc=50, scale=10, size=1000)

# Manual Stats
mean = sum(data) / len(data)
variance = sum((x - mean)**2 for x in data) / len(data)
std_dev = variance**0.5

# Visualization
plt.hist(data, bins=30, edgecolor='black')
plt.title("Normal Distribution Histogram")
plt.show()


# Manual Z-score implementation
z_scores = [(x - mean) / std_dev for x in data]

# Verification
z_mean = sum(z_scores) / len(z_scores)
z_std = (sum((z - z_mean)**2 for z in z_scores) / len(z_scores))**0.5
print(f"Standardized Mean: {z_mean:.2f}, Std Dev: {z_std:.2f}")


