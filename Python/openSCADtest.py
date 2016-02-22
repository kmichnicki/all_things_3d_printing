
def rotate(obj,angle=[0,0,0]):
    return "rotate(["+str(angle[0])+","+str(angle[1])+","+str(angle[2])+"]) "+ obj

def translate(obj, pos=[0,0,0]):
    return "translate(["+str(pos[0])+","+str(pos[1])+","+str(pos[2])+"]) "+obj

def union(obj1,obj2):
    return """union() {
"""+obj1+obj2+"""}
"""

def difference(obj1,obj2):
    return """difference() {
"""+obj1+obj2+"""}
"""

def intersection(obj1,obj2):
    return """intersection() {
"""+obj1+obj2+"""}
"""




##the stator
shight=100 #stator hight
cube1="cube([20,"+str(shight)+","+str(shight)+"],center=true); \n"
cube2="cube([20,"+str(shight-10)+","+str(shight-10)+"],center=true); \n"

x=difference(cube1,cube2)

#x=difference(x,cyls)
middleshaft="cylinder(100,3.5,3.5); \n"
x=difference(x,middleshaft)
x=rotate(x,[0,90,0])
x=translate(x,[0,0,10])
stator=x

##the jacket for the coils
chight=100 #coils hight
pthickness=6 #wall thickness of the pipe
innerradius=55
cyl="cylinder("+str(chight)+","+str(innerradius)+","+str(innerradius)+"); \n"
cyl2="cylinder("+str(chight)+","+str(innerradius+pthickness)+","+str(innerradius+pthickness)+"); \n"
jacket=difference(cyl2,cyl)

bolthole="cylinder(20,2,2); \n"
bolthole=translate(bolthole,[0,0,innerradius-10])
bolthole=rotate(bolthole,[90,0,0])
boltholes=""
for i in range(10):
    boltholes=union(boltholes,translate(bolthole,[0,0,(chight+2*i*chight)/(10*2)]))

boltholes2=""
for i in range(3):
    boltholes2=union(boltholes2,rotate(boltholes,[0,0,-7+7*i]))

boltholes2=union(boltholes2,rotate(boltholes2,[0,0,180]))
boltholes2=rotate(boltholes2,[0,0,45])

jacket=difference(jacket,boltholes2)

#subtract dowels from the jacket
dowel="cylinder(20,2,2); \n"
dowel=translate(dowel,[innerradius+pthickness/2,0,-10])
dowels=""
for i in range(4):
    dowels=union(dowels,rotate(dowel,[0,0,90*i]))

jacket=difference(jacket,dowels)
jacket=difference(jacket,translate(dowels,[0,0,chight]))



difference(jacket,dowels)

#making the endstops

endstop="cylinder(20,"+str(innerradius+pthickness)+","+str(innerradius+pthickness)+"); \n"
inner="cylinder(20,"+str(innerradius)+","+str(innerradius)+"); \n"
inner=translate(inner,[0,0,pthickness])
endstop=difference(endstop,inner)
endstop=union(translate(dowels,[0,0,20]),endstop)
endstop=difference(endstop,"cylinder(30,4.5,4.5); \n")

x=union(x,endstop)

statorfile = open('stator.scad', 'w')
#f.write("%cube([50,100,150]); \n")
statorfile.write(stator)
statorfile.close()

jacketfile = open('jacket.scad', 'w')
#f.write("%cube([50,100,150]); \n")
jacketfile.write(jacket)
jacketfile.close()

endstopfile = open('endstop.scad', 'w')
#f.write("%cube([50,100,150]); \n")
endstopfile.write(endstop)
endstopfile.close()
