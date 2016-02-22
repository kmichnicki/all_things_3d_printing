from pyscad import *


radius=7

def wing(angle,pos=[0,0,0]):
    x=cube([1,6,8],"true")
    x=translate(x,[0,0,4.5])
    x=rotate(x,[0,0,angle])
    x=translate(x,pos)
    return x



y=""
for i in range(10):
    y=union(y,wing(7+6*i,[5+7*i,0,0]))


tube=cube([72,18,10],"true")
tube=translate(tube,[0,0,3.5])

tube_cut=cylinder(72.5,7,7)
tube_cut=rotate(tube_cut,[0,90,0])
tube_cut=translate(tube_cut,[-36.25,0,7])
#tube_cut=cube([44,10,7],"true")
#tube_cut=translate(tube_cut,[0,0,5.5])

tube=difference(tube,tube_cut)
tube=translate(tube,[36,0,0])

y=union(tube,y)

y=translate(y,[-35,0,0])

y=scale(y,1)

f=open("fluidics/cascadeDiode.scad","w")
f.write(y)
f.close()


