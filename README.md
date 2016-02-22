openSCAD is not a universal programming langauge. For instance, you can't really do variables. pyscad.py is library for created openSCAD objects in and object oriented way. Objects are represented by strings and the functions in the library transform these object strings, i.e. rotates the object, cut it, union, intersection, etc... 

EXAMPLE: The following code creates a 1 by 1 by 1 cube centered at the origin, stores it in the x variable and then rotates it by 45 degrees around the Z axis. It then creates another cube stored in y variable and then takes the union of x and y. The result is translated up by 1 unit. It then writes the string to an openSCAD file. 

from pyscad import *

x=cube([1,1,1],"true")
x=rotate(x,[0,0,45])
y=cube([1,1,1],"true")
z=union(x,y)
z=translate(z,[0,0,1])

f=open("fluidics/cascadeDiode.scad","w")
f.write(z)
f.close()



 



