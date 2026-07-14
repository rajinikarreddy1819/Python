import pandas as pd

s = pd.Series([10,1,1,1,1,1,1,5]) # Series Data Structure 
print(s)

s = pd.Series([10,1,1,1,1,1,1,5, "A"])  # Transformed from int data type to String (Object) data type because of adding string to list
print(s)

s = pd.Series([10,1,1,1,1,1,1,5]) 
s.name = "Numbers"
print(s)

print(s.values)

print(s.index)

print(s[0:5:2])

print(s.iloc[3]) # returns the index value


print(s[[1,2,3]]) # Returns Multiple  values  of indices (1,2,3)


print(s.iloc[[1,2,3]]) # Returns Multiple  values  of indices (1,2,3)


index = ["apple", "banana", "Grapes", "Mango", "cherry", "Watermelon", "Pineapple", "Guva" ]

s.index = index # Adding index to list

print(s)

# print(s.iloc["Mango"]) # we can't perform label based indexing with iloc

# loc -> label based indexing your start as well as stop value both are included in the output

print(s.loc["Mango"])

print(s.loc[["Mango", "Grapes"]])

fruit_protein ={
    "Avocado": 2.0,
    "Guva": 2.6,
    "Blackberrie": 2.0,
    "Oranges": 0.9,
    "Banana": 1.1,
    "Kiwi": 1.1,
    "Apples": 0.3

}

s2 = pd.Series(fruit_protein, name ="Protein")
print(s2)

# Conditional sELECTION

print(s2>1) # returns true or false


print(s2[s2>1]) # returns values of true 

# Logical  Operators 

print((s2 > 0.5) & (s2 < 2.0))

print(s2[(s2 > 0.5) & (s2 < 2.0)])

print(s2[(s2 > 0.5) | (s2 < 2.0)])

# Modifying the series

s["Kiwi"] = 9.0
print(s["Kiwi"])


print(s.notnull().sum())
print(s2.notnull().sum())