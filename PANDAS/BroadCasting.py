import numpy as np
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlis", "David", "Eva", "Alice"],
    "Age": [25,30,35,np.nan, 29, 25],
    "Department": ["Hr", "IT", "Finance", "IT", "HR", "Hr"],
    "Salary": [50000,600000,700000,62000,np.nan,50000]
}

df = pd.DataFrame(data)

df["Salary"] = df["Salary"] + 10000
print(df["Salary"])

#Remaining the column

df.rename(columns={"Department": "Dept"}, inplace = True)
print(df)

# Check unique values

print(df["Salary"].unique())

# Checking counts of values 

print(df["Dept"].value_counts())

df["Promoted Salary"]  = df["Salary"] + 10000
print(df)

print(df.info())

