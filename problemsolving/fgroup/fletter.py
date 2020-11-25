

def letterf():
    for row in range(8):
        for col in range(11):
            if col == 0 or row == 0 or row == 3 and col > 0:
                print('*', end='')
            else:
                print(end=' ')
        print()
letterf()

# import matplotlib.pyplot as plt 
# import numpy as np 
# t = np.arange(0,2*np.pi, 0.1) 
# x = 16*np.sin(t)**3 
# y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t) 
# plt.plot(x,y) 
# plt.show() 
