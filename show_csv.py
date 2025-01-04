from numpy import genfromtxt
import matplotlib.pyplot as plt

my_data = genfromtxt('meas.csv', delimiter=' ').T
plt.plot(my_data[1]*-1,'-p', label='blue')
plt.plot(my_data[2],'--p', label='orange')
plt.plot(my_data[3], color='red', label='red')
plt.xlim(150,190)
plt.ylim(-3,3)
plt.grid()
plt.legend()
plt.show()

