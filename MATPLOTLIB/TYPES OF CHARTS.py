from matplotlib import pyplot as plt
import numpy as np
import csv

ages_x = [25,26,27,28,29,30,31,32,33,34,35]

x_indices = np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 
         62316, 64928, 67317, 68748, 73752]

plt.xlabel("Ages")
plt.ylabel("Salary")
plt.title("Medain Salary (USD) by Age")
plt.bar(x_indices - width, dev_y,width = width ,color ="Green", label ="All Devs")
plt.legend()
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 
         70003, 70000, 71496, 75370, 83640]
jav_dev_y = [49372, 58876, 58850, 50287, 63916, 75998, 
         70083, 70090, 71498, 75770, 93640]

plt.bar(x_indices , py_dev_y, color='blue', width = width,label='Python')

plt.bar(x_indices + width,  jav_dev_y, width=width, color='RED',label='JAVA')

plt.legend()
plt.xticks(ticks=x_indices, labels=ages_x)
plt.grid()
plt.tight_layout()
#plt.show()

with open('C:\Python\MATPLOTLIB\Iris.csv') as file:
    csv_reader = csv.DictReader(file)
    row = next(csv_reader)
    print(row)

