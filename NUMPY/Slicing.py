import numpy as np
array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [10,11,12]
                  ])

# array(start:end:step)
print(array[0])

print(array[0:3])

print(array[0:3:3])

print(array[::2])

print(array[::-1]) # Reverse 

print(array[-1:-4:-2])

print("====== COLUMN SELECTION =========")

# array[Row, Column]

print(array[:,0])

print(array[:,0:2])

print(array[:,0:2:2])

print(array[:, ::2])

print(array[:, ::-1]) # row reverse

print(" ================= Row Slicing And Column Slicing ==================== ")

# array[row slicing, column slicing]

print(array[1:3, 0:2])

print(array[2,:])