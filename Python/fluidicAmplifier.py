from pyscad import *


x="cylinder(2,10,10); \n"
x=translate(x,[5,0,0])
x=union(x,rotate(x,[0,0,180]))
x2=scale(x,.8)


y="cylinder(2,4,4); \n"
y=translate(y,[1.5,0,0])
y=union(y,rotate(y,[0,0,180]))

y=translate(y,[0,-18,0])




upper2="cube([25,6,2],center=true); \n"
upper3=rotate(upper2,[0,0,30])
upper3=translate(upper3,[3,0,0])
upper3=union(upper3,rotate(upper3,[0,180,0]))
upper3=translate(upper3,[0,12,1])

#upper4="cube([16,6,2],center=true); \n"
#upper4=translate(upper4,[16.3,15.6,0])
#upper4=union(upper4,rotate(upper4,[0,180,0]))
#upper4=translate(upper4,[0,0,1])

middle="cube([6,43,2],center=true); \n"
middle=translate(middle,[0,-7,1])
middle2="cube([6,10,2],center=true); \n"
middle2=rotate(middle2,[0,0,-12])
middle2=translate(middle2,[1,-13,0])
middle2=union(middle2,rotate(middle2,[0,180,0]))
middle2=translate(middle2,[0,0,1])

middle=union(middle,middle2)

uppermiddle="cube([1.5,15,2],center=true); \n"
uppermiddle2="cube([3,8,2],center=true); \n"
uppermiddle=union(uppermiddle,uppermiddle2)
uppermiddle=translate(uppermiddle,[0,15,1])

middle=union(middle,uppermiddle)

x=union(x,y)
x=union(x,upper3)
#x=union(x,upper4)
x=union(x,middle)


lowerbar="cube([30,2,2],center=true); \n"
lowerbar=translate(lowerbar,[0,-18,1])
x=union(lowerbar,x)
x=translate(x,[0,0,2.01])

plate="cube([40,65,4],center=true); \n"
plate=translate(plate,[0,-2,0])
##plate1="cube([20,25.5,6],center=true); \n"
##plate1=translate(plate1,[27,-2,0])
##plate1=union(plate1,rotate(plate1,[0,180,0]))
##
##plate=difference(plate,plate1)
##
##plate2="cube([15,10,6],center=true); \n"
##plate2=translate(plate2,[13.5,-27,0])
##plate2=union(plate2,rotate(plate2,[0,180,0]))
##
##plate=difference(plate,plate2)
##
##plate3="cube([18,10,6],center=true); \n"
##plate3=translate(plate3,[12,26,0])
##plate3=union(plate3,rotate(plate3,[0,180,0]))
##
##plate=difference(plate,plate3)
##
##
plate=translate(plate,[0,0,2])
x=difference(plate,x)

nozzle=cylinder(2,6,6)
nozzle=union(nozzle,cylinder(20,3,3))
nozzle=difference(nozzle,cylinder(20,2,2))
nozzle=translate(nozzle,[0,50,0])

fnozzle=nozzle
for i in range(7):
    fnozzle=union(fnozzle,rotate(nozzle,[0,0,360*i/7]))
    

x=union(x,fnozzle)

f=open("fluidics/fluidicAmplifier.scad","w")
f.write(x)
f.close()
