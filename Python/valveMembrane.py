from pyscad import *



##First valve membrane
##u="cylinder(30,50,50,$fn=50); \n"
##v="cylinder(30,49,49,$fn=50); \n"
##u=difference(u,v)
##u=translate(u,[0,50.6,-15])
##u=union(u,rotate(u,[0,0,180]))
##u=rotate(u,[0,90,0])
##
##cuttop="cube([100,100,100],center=true); \n"
##cuttop=translate(cuttop,[0,0,50])
##u=difference(u,cuttop)
##u=translate(u,[0,0,10])
##x="cube([30,10,30],center=true); \n"
##y="cube([28,8,30],center=true); \n"
##y=difference(x,y)
##
##u=intersection(u,x)
##
##final=union(u,y)
##
##final=translate(final,[0,0,15])
##final=union(final,"%cube(40,60,80); \n")
##
##
##
##f=open("valveMembrane.scad","w")
##f.write(final)
##f.close()


u="cylinder(30,50,50,$fn=50); \n"
v="cylinder(30,49,49,$fn=50); \n"
u=difference(u,v)
u=translate(u,[0,50.25,-15])
u=union(u,rotate(u,[0,0,180]))
u=rotate(u,[0,90,0])

cuttop="cube([100,100,100],center=true); \n"
cuttop=translate(cuttop,[0,0,50])
u=difference(u,cuttop)
u=translate(u,[0,0,8])
x="cube([30,10,25],center=true); \n"
y="cube([28,8,25],center=true); \n"
y=difference(x,y)

u=intersection(u,x)

final=union(u,y)

final=translate(final,[0,0,12.5])
final=union(final,"%cube(40,60,80); \n")

final=scale(final,1.1)

f=open("valveMembrane.scad","w")
f.write(final)
f.close()
