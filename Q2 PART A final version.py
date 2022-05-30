import numpy as np
import time as t
start_time=t.time()
k=((np.pi)/180)
l1=1.2
l2=1.6

t1=k*34
t2=22*k
 
T=np.array([[np.cos(t1),-np.sin(t1),0,l1*np.cos(t1)],[np.sin(t1),np.cos(t1),0,l1*np.sin(t1)],[0,0,1,0],[0,0,0,1]])
pos=np.array([l2*np.cos(t2*np.pi/180),l2*np.sin(t2*np.pi/180),0,1])
newpos=np.array([0,0,0,0])

newpos=np.dot(T,pos)
print("x co-ordinate: ",newpos[0],",y co-ordinate: ",newpos[1])
print("--- %s ---"% (t.time()-start_time))