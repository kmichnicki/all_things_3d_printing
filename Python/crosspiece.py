from pyscad import *
import math

scale=10
t=.2
w=1
h=4

t=scale*t
w=scale*w
h=scale*h

x=cube([w,h,t],'true')

x1=cube([w,h,1.2*t],'true')#The piece we use to cut away

x=translate(x,[0,0,t/2])

x1=translate(x1,[0,0,1.2*t/2])



y=rotate(x,[90,0,0])

y1=rotate(x1,[90,0,0])


y=translate(y,[float(w)/2,float(h)/4,0])

y1=translate(y1,[float(w)/2,float(h)/4,0])

z=rotate(y1,[0,0,180])
y=union(y,z)

x=difference(x,y)

x=union(x,rotate(x,[0,0,90]))
x=translate(x,[-45,-45,0])

y=""
for i in range(3):
    for j in range(3):
        y=union(y,translate(x,[45*i,45*j,0]))
    
        


f=open("crosspiece.scad","w")
f.write(y)
f.close()
