import numpy as np
array= np.array([[1,3,4,5,56,6], [3,4,45,6,67,78]])

print("SUM OF ALL ELES:", np.sum(array))
print("SUM OF 2 COL: " , np.sum(array[1]))
print(np.mean(array))
print(np.std(array))
print(np.max(array))
print(np.min(array))
print(np.argmax(array)) # Return the Max number index from list
print(np.argmin(array)) # Return the Max number index from list

print(np.sum(array, axis=0)) # Returns list of sum of columns [(1+3), (3+4),.....]

print(np.sum(array, axis=1)) # Returns list of sum of columns [(1+3), (3+4),.....]
