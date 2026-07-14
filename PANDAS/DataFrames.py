# dataframe
import numpy as np
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlis", "David", "Eva", "Alice"],
    "Age": [25,30,35,np.nan, 29, 25],
    "Department": ["Hr", "IT", "Finance", "IT", "HR", "Hr"],
    "Salary": [50000,600000,700000,62000,np.nan,50000]
}

df = pd.DataFrame(data)
print(df)
print(df.head(3))
print(df.tail(4))

# iloc and loc

print(df.iloc[1:4:2])
print(df.loc[1:3,["Age", "Department"]])

print(df["Age"])
print(df[["Age", "Department"]])
print(df.drop("Age", axis =1)) # Age is not dropped
print(df.drop("Age", axis =1, inplace = True)) #inplace attribute helps to perfom operation on real dataframe
print(df)

print(df.info())

print(df.shape)

print(df.describe())