import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print(arr1.shape) # Both 
print(arr2.shape)
print(arr1 + arr2)


arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8,9])
print(arr1.shape) # Both 
print(arr2.shape)
# print(arr1 + arr2) Both shapes are not same 

arr1 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15]])
arr2 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15]
                 ])

print(arr1.shape) 
print(arr1.size)
print(arr2.size)
print(arr2.shape)
print(arr1 + arr2) # Both Shapes are Same so we do manipulations easily


print("==================== CASE 2 ====================================")
arr1 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15]])
arr2 = np.array([[1,2,3,4,5]
                ])

print(arr1.shape)  # Shape = 
print(arr1.size) # (ROWS = 3, COLS = 5)
print(arr2.size) # (ROWS = 1 COLS = 5)
print(arr2.shape)


""""

 Arr1:

[1,2,3,4,5],
[6,7,8,9,10],        Rows = 3 And Cols = 5           
[11,12,13,14,15]    

Arr2: 

[1,2,3,4,5]   Rows = 1 and Cols = 5


This case applicable if one of two arrays of rows or cols have 1 


Here Rows of Arr2 is 1 so then Numpy automatically copy the exists eles [1,2,3,4,5] and conver into [1,2,3,4,5] To match number of rows equivalent to other array consists of
                                                                                                    [1,2,3,4,5] 
                                                                                                    [1,2,3,4,5]


Number of Cols for both arrays have same so nothing can done


For Cols (if arr1 cols = 1 and arr2 cols = 5)

it will convert from [1]  to [1,1,1,1,1]
                     [2]     [2,2,2,2,2]
                     [3]     [3,3,3,3,3]




"""

print(arr1 + arr2) # Both rows and cols are different but either both rows and cols of two arrays have same number of rows or cols then we can do  manipulations by copying existing elemets in list until we match  both number of rows and cols 



print("=========================================== CASE 3 ==========================================================")
arr1 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15]])
arr2 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15], 
                 [16,17,18,19,20]
                 ])

print(arr1.shape) 
print(arr1.size) # ROWS = 3  COLS = 5
print(arr2.size) # ROWS = 4  COLS = 5
print(arr2.shape)

""""  Number of rows and cols for both arrays are not same and also there is no numbers of rows and cols equal to 1, so we can not perform manipulation  """
# print(arr1 + arr2) 
