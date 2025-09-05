import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(loc=0, scale=1, size=100)
print(data)
plt.scatter(np.arange(0, 100), data)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Scatter plot of data')
plt.show()
