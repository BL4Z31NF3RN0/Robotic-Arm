import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as an
import math as m
xi=50
yi=-(m.sqrt(3600-2500))
x_data = [0,xi,100]
y_data =[0,yi,0]

fig, ax= plt.subplots()
ax.set_xlim(-200, 200)
ax.set_ylim(-200, 200)
line, = ax.plot(0,0)


def animation_frame(i):
#  if 5*i!=5000:
   
    y=50
    if i<=50:
     i2=100-(4*i)
  
     r=m.sqrt((i2*i2)+(y*y))
     x_data.pop(2)
     x_data.insert(2,i2)
     x_data.pop(1)
     x_data.insert(1,i2/2)
     y_data.pop(1)
     y_data.insert(1,-m.sqrt(70.8**2-((i2/2))**2))
    else:
        i=i-50
        i2=m.pi-(i/80)
        x=100*m.cos(i2)
        y=20*m.sin(i2)
        r=m.sqrt(x**2+y**2)
        r1=m.sqrt(60**2-(r/2)**2)
        sl=y/x
        if sl!=0:
         sl1=-1/sl
         th=m.atan(sl1)
         w=(x/2)-(r1*m.cos(th))
         g=(y/2)-(r1*m.sin(th))
        else:
         w=50
         g=-(m.sqrt(3600-2500))
        x_data.pop(1)
        x_data.insert(1,w)
        y_data.pop(1)
        y_data.insert(1,g)

        x_data.pop(2)
        x_data.insert(2,x)
        y_data.pop(2)
        y_data.insert(2,y)
    
  #else:
  # an.pause()
 
     

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line, 

animation = FuncAnimation(fig, func=animation_frame, frames=290, interval=4)
plt.show()
