difference() {
translate([0,0,2]) cube([25,35,4],center=true); 
translate([-3,-1,2]) scale(0.3) linear_extrude(height = 40) import("test4.dxf");}
