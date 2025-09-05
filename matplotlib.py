# all my imports
import numpy as np
import matplotlib.pyplot as plt
# linear array of 100 elements from normal distribution
data = np.random.normal(loc=0, scale=1, size=100)
print(data)
#scatter plot of data against its indices
plt.scatter(np.arange(0, 100), data)
# assiging labels to x and y
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Scatter plot of data')
# printing plot
plt.show()
