union() {
translate([0,0,10]) rotate([0,90,0]) difference() {
difference() {
cube([20,100,100],center=true); 
cube([20,80,90],center=true); 
}
cylinder(100,3.5,3.5); 
}
difference() {
union() {
translate([0,0,20]) union() {
union() {
union() {
union() {
rotate([0,0,0]) translate([58,0,-10]) cylinder(20,2,2); 
}
rotate([0,0,90]) translate([58,0,-10]) cylinder(20,2,2); 
}
rotate([0,0,180]) translate([58,0,-10]) cylinder(20,2,2); 
}
rotate([0,0,270]) translate([58,0,-10]) cylinder(20,2,2); 
}
difference() {
cylinder(20,61,61); 
translate([0,0,6]) cylinder(20,55,55); 
}
}
cylinder(30,4.5,4.5); 
}
}
