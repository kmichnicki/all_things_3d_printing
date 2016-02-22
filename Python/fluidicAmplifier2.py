from pyscad import *


x="linear_extrude(height = 40) import(\"test4.dxf\");"
x=scale(x,.3)
x=translate(x,[-3,-1,2])

c=cube([25,35,4],"true")
c=translate(c,[0,0,2])
x=difference(c,x)

f=open("fluidics/Amplifier5.scad","w")
f.write(x)
f.close()
