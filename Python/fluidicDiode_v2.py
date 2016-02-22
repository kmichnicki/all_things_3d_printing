from pyscad import *


def top():
    x=vectorCylinder([0,0,0],[0,0,2],70,70)
    inlet=cube([8,70,2])
    inlet=translate(inlet,[62,0,0])
    x=union(x,inlet)

    y=vectorCylinder([0,0,2],[0,0,22],5,5)
    
    x=union(x,y)

    cut=vectorCylinder([0,0,-2],[0,0,24],3,3)
    x=difference(x,cut)
    return x


def bottom():
    x=vectorCylinder([0,0,0],[0,0,7],70,70)
    x_cut=vectorCylinder([0,0,2],[0,0,10],68,69)

    #inlet=vectorCylinder([70,65,4],[0,65,4],4,4)
    #inlet_cut=vectorCylinder([70,65,4],[0,65,4],2,2)
    inlet=cube([9,70,7])
    inlet=translate(inlet,[62,0,0])

    inlet_cut=cube([4,80,4.2])
    inlet_cut=translate(inlet_cut,[64.3,0,2.8])

    
    x=union(x,inlet)
    cuts=union(x_cut,inlet_cut)
    x=difference(x,cuts)
    
    return x










f=open("fluidicDiode_v2_top2.scad","w")
f.write(top())
f.close()

f=open("fluidicDiode_v2_bottom2.scad","w")
f.write(bottom())
f.close()
