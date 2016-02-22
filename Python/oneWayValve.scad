difference() {
difference() {
cylinder(20,5,0); 
translate([0,0,-2]) cylinder(20,5,0); 
}
translate([0,0,15]) union() {
cube([.6,15,15],center=true); 
cube([15,.6,15],center=true); 
}
}
