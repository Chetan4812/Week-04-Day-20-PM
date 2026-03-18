marks = np.random.randint(0, 100, 100)
m_mean = np.mean(marks)
m_std = np.std(marks)

# Outlier Detection (|Z| > 2)
outliers = [x for x in marks if abs((x - m_mean) / m_std) > 2]
