import numpy as np

# Scaler Arthmetic

array= np.array([1,2,3,4])

print(array + 1)

print(array * 2)

print(array / 2)

print("============ Vectorized Math Functions ============")
# Vectorized Math Functions

print(np.sqrt(array))

print(np.round(array))

print(np.floor(array))

print(np.pi * array ** 2) # A = PIR2

print("================= ELEMENT WISE ARITHMETIC =======================")

# ELEMENT WISE ARITHMETIC

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)


print(" =================== Comparsion Operators =============")

scores = np.array([91,90,89,60,45,100,78,86])

scores[scores < 60] = 0

print(scores)

print(scores >= 60)
