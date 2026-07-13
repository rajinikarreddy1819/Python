import numpy as np 

rng = np.random.default_rng()

print(rng.integers(low = 1, high=100, size=3))

rng = np.random.default_rng(seed=1)

print(rng.integers(low = 1, high=100, size=3))

print(np.random.uniform(low = -1, high =1001, size=100))