from matplotlib import pyplot as plt

ages_x = [25,26,27,28,29,30,31,32,33,34,35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 
         62316, 64928, 67317, 68748, 73752]

plt.xlabel("Ages")
plt.ylabel("Salary")
plt.title("Medain Salary (USD) by Age")
plt.plot(ages_x, dev_y, color = 'green', linestyle='--' , marker = '.',label='ALL Devs')
plt.legend()


plt.style.use()
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 
         70003, 70000, 71496, 75370, 83640]

plt.xlabel("Ages")
plt.ylabel("Salary")
plt.title("Medain Salary (USD) by Age")

plt.plot(ages_x, py_dev_y, color='blue', linestyle="--",linewidth=3,marker = '.',label='Python')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()







