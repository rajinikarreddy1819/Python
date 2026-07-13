import numpy as np
ages = np.array([[21,7,33,60,56,20,99,30],
                [39,45,65,67,88,45,33,26]] )

teenagers = ages[ages < 18]
print(teenagers)

Adults = ages[(ages >= 18) & (ages < 65)]
print(Adults)

seniors = ages[ages >= 65]
print(seniors)


adults = np.where( ages >= 18, ages, -1)
print(adults)