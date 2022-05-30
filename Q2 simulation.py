import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as an
import math as m

x_data = [0,1.2,2.8]
y_data =([0,0,0])

fig, ax= plt.subplots()
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
line, = ax.plot(0,0)


def animation_frame(i):
#  if 5*i!=5000:
    t1=34
    t2=22
    x_data.pop(1)
    x_data.insert(1,(1.2*m.cos(i*4*t1/500/180*m.pi)))
    y_data.pop(1)
    y_data.insert(1,(1.2*m.sin(i*4*t1/500/180*m.pi))) 
    x_data.pop(2)
    x_data.insert(2,(1.2*m.cos(i*4*t1/500/180*m.pi))+(1.6*m.cos((i*4*t1/500/180*m.pi)+(i*4*t2/500/180*m.pi))))
    y_data.pop(2)
    y_data.insert(2,(1.2*m.sin(i*4*t1/500/180*m.pi))+(1.6*m.sin((i*4*t1/500/180*m.pi)+(i*4*t2/500/180*m.pi)))) 
  #else:
  # an.pause()
 
     

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line, 

animation = FuncAnimation(fig, func=animation_frame, frames=125, interval=5)
plt.show()
