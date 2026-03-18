rejections = 0
for _ in range(1000):
    sample = np.random.normal(50, 10, 30)
    z_stat = (np.mean(sample) - 50) / (10 / (30**0.5))
    if abs(z_stat) > 1.96:
        rejections += 1

fpr = rejections / 1000
print(f"False Positive Rate: {fpr}")
