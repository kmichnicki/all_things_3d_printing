difference() {
translate([0,0,2]) cube([20,30,4],center=true); 
translate([0,0,2]) scale(0.2) linear_extrude(height = 30) import("test.dxf");}
