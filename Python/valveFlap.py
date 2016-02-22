from pyscad import *

x="cube([10,10,40],center=true); \n"
x2="cube([8,8,40],center=true); \n"
x=difference(x,x2)

y="cube([100,100,100],center=true); \n"
y=translate(y,[0,0,50])
y=rotate(y,[60,0,0])
y=translate(y,[0,0,11])
x=difference(x,y)

u="cube([12,1.2,50],center=true); \n"
u=rotate(u,[-28,0,0])
u=translate(u,[0,-8.5,0])
x=union(x,u)
cut="cube([100,100,50],center=true); \n"
cut=translate(cut,[0,0,5])
x=intersection(x,cut)


v="cube([16,28,48],center=true); \n"
v2="cube([14,26,48],center=true); \n"
v2=translate(v2,[0,0,2])
v=difference(v,v2)
v=translate(v,[0,-6,4])
x=union(x,v)
x2=translate(x2,[0,0,-30])
x=difference(x,x2)
x=translate(x,[0,0,20])
x=union(x,"%cube([20,30,40]); \n")


f=open("valveFlap.scad","w")
f.write(x)
f.close()
