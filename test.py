import numpy as np
import matplotlib.pyplot as plt

# Parameters for the wave
x = np.linspace(0, 10, 1000)  # x values
amplitude = np.random.uniform(0.5, 1.5)  # random amplitude
frequency = np.random.uniform(1, 3)  # random frequency
phase = np.random.uniform(0, 2 * np.pi)  # random phase

# Generating the wavy line with some randomness
y = amplitude * np.sin(frequency * x + phase) + np.random.normal(0, 0.2, x.shape)

# Plotting the wavy line
plt.plot(x, y)
plt.title("Random Wavy Line")
plt.show()