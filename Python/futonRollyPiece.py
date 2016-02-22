from pyscad import *


x=cylinder(32.5,12.25,12.25)
x=difference(x,cylinder(50,2.5,2.5))
y=cylinder(50,3.75,3.75)
y=translate(y,[0,0,16.25])
x=difference(x,y)

z=difference(cylinder(3.75,17,17),cylinder(3.75,12.4,12.4))
z=translate(z,[40,0,0])

x=union(x,z)

f=open("futonRolly.scad","w")
f.write(x)
f.close()
