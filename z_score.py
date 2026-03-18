def z_score(x, mean, std):
    """Returns the standardized value (Z-score) of x."""
    return (x - mean) / std

# Applying to a dataset
dataset = [10, 20, 30, 40, 50]
d_mean = sum(dataset) / len(dataset)
d_std = (sum((x - d_mean)**2 for x in dataset) / len(dataset))**0.5

standardized_data = [z_score(val, d_mean, d_std) for val in dataset]
print(f"Standardized Dataset: {standardized_data}")
