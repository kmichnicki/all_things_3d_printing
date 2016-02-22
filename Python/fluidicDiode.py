from pyscad import *


def fluidicDiode(isout=1):
    if isout==0:
        scale1=1
        scale2=1
    else:
        scale1=1.2
        scale2=1.5

    #base
    if isout==1:
        x=""
    else:
        x=eyeCylinder(40,5) #inlet
        x=rotate(x,[90,0,0])
        x=translate(x,[0,0,5])

    y=eyeCircle(scale1*30) #drum
    y=translate(y,[0,0,30])

    z=eyeCylinder(20,scale2*5)
    z1=translate(z,[0,0,-20])
    z1=rotate(z1,[0,90,0])
    z1=rotate(z1,[90,0,0])
    z1=translate(z1,[20,0,30])

    if isout==1:
        z2=rotate(eyeCylinder(80,scale2*6),[0,0,90])
        z2=translate(z2,[15,0,-2])
    else:
        z2=rotate(eyeCylinder(50,scale2*5),[0,0,90])
        z2=translate(z2,[15,0,30])

    x=union(x,y)
    x=union(x,z1+z2)

    if isout==1:
        c=cube([8,70,14],"true")
        c=translate(c,[0,-4,5])
        
        x=union(x,c)
        x=difference(x,translate(c,[0,0,-14]))
        

    else:
        x=translate(x,[0,0,0])
    

    return x


out=difference(fluidicDiode(1),fluidicDiode(0))

out=translate(out,[0,0,2])











out=union(out,"%cube([30,40,50]); \n")

f=open("fluidDiode.scad","w")
f.write(out)
f.close()
