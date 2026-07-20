import numpy as np
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlis", "David", "Eva", "Alice"],
    "Age": [25,30,35,np.nan, 29, 25],
    "Department": ["Hr", "IT", "Finance", "IT", "HR", "Hr"],
    "Salary": [50000,600000,700000,62000,np.nan,50000]
}

df = pd.DataFrame(data)
df["Promoted Salary"]  = df["Salary"] + 10000
# Checking Null Values 

print(df.isnull().sum())

print(df.dropna(how="any")) # This operation performs on duplicate Dataframe not original one
print(df) # Real dataframe is not deleted 

# Missing can be filled with 1. Getting rid off them
# 2. fillinf up  with max/min/mean/avg values of columns
print(df["Age"].fillna(18)) # Fills the missing values with 18 
# print(df.fillna(0)) # fills all nan values with 0 value
print(df["Age"].fillna(df["Age"].mean()))
print(df["Salary"].fillna(df["Salary"].median()))


# 3. Forwad Filling means filling the Nan value with upper value if it is Not Null value

print(df["Age"].ffill())

print(df)

# 4. Backward Filling means filling the Nan value with below value if it is Not Null value


print(df["Age"].bfill())

# Replace the Columns 

print("=============== Before ===================")
print(df["Name"])

df["Name"] = df["Name"].replace("Charlis", "Rose") # Original Dataframe will change because of Assiging to Name after manipulation

print("=============== After ===================")

print(df["Name"])

df_dup = df[df.duplicated(keep="first")] # Returns entire row if both entire rows have same values
 # here keep attribute decides from where to start 
# first means starts from first row to last row. It will return duplicate as last value
print(df_dup) # Returned Last index (5)

# last means starts from last row to first row. It will return duplicate as first value
df_dup = df[df.duplicated(keep="last")] 
print(df_dup) # Returned First index

print(df.drop_duplicates(keep="first")) # keep attribute : "first" (Default)

df = df.drop_duplicates(keep="last")

print(df)


#Invalid Values

df["Promoted Salary"] = df["Promoted Salary"].apply(lambda x: x/10 if x > 65000 else x )
print(df["Promoted Salary"])


df["Name"] = df["Name"].replace("Alice", "Alice_Usagi")

 # df[["first_name", "last_name"]] = df["Name"].str.split("_")

def multiplying_age(x):
    return x*2
df["Age"] = df["Age"].apply(multiplying_age)
print(df["Age"])

df["Age"] = df["Age"].apply(lambda x:x/2)
print(df["Age"])


