from pyscad import *
import math




class curve1:
    
    def fun(self, v=[.9,.9,.9]):
        scale=10
        theta=.4*v[2]
        center=4
        return [scale*v[0],scale*(center-(center-v[1])*math.cos(theta)),scale*(center-v[1])*math.sin(theta)]
       
class curve2:
    def fun(self, v=[.9,.9,.9]):
        scale=10
        theta=.4*v[2]
        center=-2
        return [scale*v[0],scale*(center-(center-v[1])*math.cos(theta)),-scale*(center-v[1])*math.sin(theta)]

class curve3:
    def fun(self, v=[.9,.9,.9]):
        scale=10
        return [scale*v[0],scale*v[1],scale*v[2]]

def stabColor(v,u,stab):
    normsquared=(v[0]-u[0])**2+(v[1]-u[1])**2+(v[2]-u[2])**2
    

    if stab==1 and normsquared==1 and ((v[0]==1 and v[1]==1 and v[2]==1) or (u[0]==1 and u[1]==1 and u[2]==1)):
        rr=[.9,.9,.9]
    elif stab==1 and normsquared==1 and v[0]==0 and ( (v[2]==2 and u[2]==3 and (v[1]==1 or v[1]==2)) or (v[1]==1 and u[1]==2 and (v[2]==2 or v[2]==3)) ):
        rr=[.9,.9,.9]
    elif normsquared==1 and v[0]==0 and v[1]==0 and (u[2]-v[2])==1:
        rr=[0,0,0]
    else:
        rr=[.9,.9,.9]

    return rr


def theCode(c,stab=0,logical=0):
    scale=10
    radius=.05*scale
    size=3
    zsize=size+3
    out2=""
    for i in range(size):
        for j in range(size):
            
            if (i==0 and j==0 and logical==1): #mark logical operator
                clr=[0,0,0]
            else:
                clr=[.9,.9,.9]

            
                
            out2=out2+color(vectorCylinder(c.fun([i,j,0]),c.fun([i,j,.5]),radius,radius),clr)
            out2=out2+color(vectorCylinder(c.fun([i,j,zsize-.5]),c.fun([i,j,zsize]),radius,radius),clr)
            for k in range(zsize):
                
                if k<zsize-1:
                    clr=stabColor([i,j,k],[i,j,k+1],stab) #set color of stabilizers and logical operators
                    out2=out2+color(vectorCylinder(c.fun([i,j,k+.5]),c.fun([i,j,k+1.5]),radius,radius),clr)
                if i<size-1:
                    clr=stabColor([i,j,k],[i+1,j,k],stab)
                    out2=out2+color(vectorCylinder(c.fun([i,j,k+.5]),c.fun([i+1,j,k+.5]),radius,radius),clr)
                    
                if j<size-1:
                    clr=stabColor([i,j,k],[i,j+1,k],stab)
                    out2=out2+color(vectorCylinder(c.fun([i,j,k+.5]),c.fun([i,j+1,k+.5]),radius,radius),clr)
    return out2      
                    

C1=curve1()
C2=curve2()
C3=curve3()
        
out2=theCode(C3,1,1)
out2=union(out2,theCode(C1,0,1))
out2=union(out2,theCode(C2,0,1))

f=open("WeldedCodes/welded.scad","w")
f.write(out2)
f.close()


D1=curve3()

out=theCode(D1)
f=open("WeldedCodes/single.scad","w")
f.write(out)
f.close()
