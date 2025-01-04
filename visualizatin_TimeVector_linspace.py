import numpy as np
import matplotlib.pyplot as plt

f_s = 20
T = 6.24

t = np.linspace(0, T, int(T*f_s), endpoint=False)
y = np.sin(t)

plt.plot(t,y,'-p',label=f'f=1Hz')

f_s = 5
T = 1.5*6.24
t = np.linspace(0, T, int(T*f_s), endpoint=False)
y = np.sin(2*t)

plt.plot(t,y,'-p', label=f'f=2Hz')

mean = np.mean(y*y)
plt.plot(t,y*y,'--p',color='magenta',label=f'mean(1Hz * 1Hz)={mean}')

plt.xlim(0,2*3.14)
plt.ylim(-1.5,1.5)
plt.title('sinusoids')
plt.axhline(y=0,color='black')
plt.grid()
plt.legend()
plt.show()