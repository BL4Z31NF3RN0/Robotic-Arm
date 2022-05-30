import numpy as np
import time as t
start_time=t.time()
k=((np.pi)/180)
l1=float(input("enter l1\n"))
l2=float(input("enter l2\n"))
c=int(input("will you be entering angle in:\n1)degrees\n2)radians\nenter the number in front of your prefered units\n"))
if c==1:
    t1=float(input("enter theta 1\n"))*k
    t2=float(input("enter theta 2\n"))*k

 
elif c==2:
  t1=float(input("enter theta 1\n"))
  t2=float(input("enter theta 2\n"))
 
T=np.array([[np.cos(t1),-np.sin(t1),0,l1*np.cos(t1)],[np.sin(t1),np.cos(t1),0,l1*np.sin(t1)],[0,0,1,0],[0,0,0,1]])
pos=np.array([l2*np.cos(t2*np.pi/180),l2*np.sin(t2*np.pi/180),0,1])
newpos=np.array([0,0,0,0])

newpos=np.dot(T,pos)
print("x co-ordinate: ",newpos[0],",y co-ordinate: ",newpos[1])
print("--- %s ---"% (t.time()-start_time))