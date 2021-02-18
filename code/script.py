import numpy as np

a = np.zeros(2, 3)


for i in range(100):
    a = a * i


print(a)
