import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
x = np.arange(0, 10, 1)
y = x ** 2

# Plot
plt.plot(x, y, marker='o')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Python Plot")

# Save and show
plt.savefig("plot.png")
plt.show()
