import math


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

def scale(obj,num):
    return "scale("+str(num)+") "+obj

def cylinder(h,r1,r2,center="false",resolution=.02):
    return "cylinder("+str(h)+","+str(r1)+","+str(r2)+",center="+str(center)+",$fs="+str(resolution)+"); \n"

def sphere(resolution=20):
    return "sphere("+str(r)+",$fs="+str(resolution)+"); \n"

def cube(p=[1,1,1],center="false"):
    return "cube(["+str(p[0])+","+str(p[1])+","+str(p[2])+"],center="+center+"); \n"


def eyeCircle(r):
    """this is two spheres intersecting to form a cavitt that can be 3d printed."""
    x=sphere(2*r)
    x=translate(x,[r*math.sqrt(3),0,0])
    x=intersection(x,rotate(x,[0,0,180]))
    return x

def eyeCylinder(length,h1):
    """this is two cylinders intersected to form a tube that can be 3d printed."""
    x=cylinder(length,2*h1,2*h1)
    x=translate(x,[h1*math.sqrt(3),0,0])
    x=intersection(x,rotate(x,[0,0,180]))
    return x

def vectorCylinder(x=[0,0,0],y=[0,0,1],r1=1,r2=1):
    """Allows you to position the endpoints of a cylinder"""
    if (x[0]==y[0] and x[1]==y[1] and x[2]==y[2]) or (r1==0 and r2==0): #the cylinder has no depth
        print "ERROR:the cylinder has no depth or width. Either the end points start and end at the same location or both radii are zero."
        exit()
    
    height=math.sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2 + (y[2]-x[2])**2 )
    cyl=cylinder(height,r1,r2)
    cross=[-(y[1]-x[1]),y[0]-x[0],0]#cross product with the z-axis
    dot=y[2]-x[2] #the dot product of the cylinder with the vertical

    if cross[0]==0 and cross[1]==0: #the vector is in the z-direction
        if dot<0:
            cyl=rotate(cyl,[0,180,0])

    else:
        norm=math.sqrt(cross[0]**2+cross[1]**2+cross[2]**2)
        angle=(180/math.pi)*math.asin(norm/height)
        if dot<0:
            angle=180-angle
        
        normal=[cross[0]/norm,cross[1]/norm,cross[2]/norm]
        cyl="rotate("+str(angle)+",["+str(normal[0])+","+str(normal[1])+","+str(normal[2])+"]) { \n "+cyl+ "\n }"

    if x != [0,0,0]:
        cyl=translate(cyl,x)
    return cyl

def color(x,v=[1,1,1]):
    return "color(["+str(v[0])+","+str(v[1])+","+str(v[2])+"]){"+x+"} \n"
        
            


    




