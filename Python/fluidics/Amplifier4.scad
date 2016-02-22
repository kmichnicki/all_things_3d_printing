difference() {
translate([0,0,2]) cube([25,35,4],center=true); 
translate([0,-5,2]) scale(0.25) linear_extrude(height = 40) import("test3.dxf");}
