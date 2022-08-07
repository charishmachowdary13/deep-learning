# -*- coding: utf-8 -*-
"""dl assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lWeqabb6MunMVFGJ12FeKWF1W10nAaXc
"""

import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import axes3d,Axes3D
plt.rcParams.update({'font.size':15})

x=np.arange(-1,1,0.001)
h11=1/(1+np.exp(-(500*x+30)))
h12=1/(1+np.exp(-(500*x-30)))
h21=h11-h12

plt.figure(figsize=(10,10))

plt.subplot(311)
plt.ylabel("$h_{11}(x)$")
plt.title("part (a)")
plt.plot(x,h11)

plt.subplot(312)
plt.ylabel("$h_{12}(x)$")
plt.plot(x,h12,"g-")

plt.subplot(313)
plt.ylabel("$h_{21}(x)$")
plt.xlabel("$X$")
plt.plot(x,h21,"r-")

plt.show()

import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import axes3d,Axes3D
plt.rcParams.update({'font.size':15})

def h11(x1,x2):
  return 1/(1+np.exp(-(x1+50*x2+100)))

def h12(x1,x2):
  return 1/(1+np.exp(-(x1+50*x2-100)))

def h13(x1,x2):
  return 1/(1+np.exp(-(50*x1+x2+100)))

def h14(x1,x2):
  return 1/(1+np.exp(-(x1+50*x2-100)))

def h21(x1,x2):
  return h11(x1,x2)-h12(x1,x2)

def h22(x1,x2):
  return h13(x1,x2)-h14(x1,x2)

def h31(x1,x2):
  return h21(x1,x2)+h22(x1,x2)

def f(x1,x2):
  return 1/(1+np.exp(-(100+h31(x1,x2)-200)))

x1=np.arange(-5,5,0.001)
x2=np.arange(-5,5,0.001)
X,Y=np.meshgrid(x1,x2)

Z=h11(X,Y)

fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(X,Y,Z)
ax.set_xlabel('$x_1$',fontsize=18)
ax.set_ylabel('$x_2$',fontsize=18)
ax.set_zlabel('$h_{11}$',fontsize=18)





