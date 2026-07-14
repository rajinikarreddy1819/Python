import numpy as np
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlis", "David", "Eva", "Alice"],
    "Age": [25,30,35,np.nan, 29, 25],
    "Dept": ["Hr", "IT", "Finance", "IT", "HR", "Hr"],
    "Salary": [50000,600000,700000,62000,np.nan,50000]
}

df = pd.DataFrame(data)
df["Promoted Salary"]  = df["Salary"] + 10000

depart_info = {
    "Dept": ["HR", "IT", "Finance"],
    "Location": ["New York", "San Francisco", "Chicago"],
    "Manager": ["Laura", "steve", "Nina"]
}

df2 = pd.DataFrame(depart_info)

print(pd.concat([df,df2]))

print(pd.concat([df, df2], axis = 1))

merge = pd.merge(df,df2, on = "Dept") # Merging the Data based on the Dept
print(merge)


