union() {
translate([0,0,2]) difference() {
difference() {
union() {
union() {
union() {
translate([0,0,30]) intersection() {
translate([62.3538290725,0,0]) sphere(72.0); 
rotate([0,0,180]) translate([62.3538290725,0,0]) sphere(72.0); 
}
}
translate([20,0,30]) rotate([90,0,0]) rotate([0,90,0]) translate([0,0,-20]) intersection() {
translate([12.9903810568,0,0]) cylinder(20,15.0,15.0,center=false); 
rotate([0,0,180]) translate([12.9903810568,0,0]) cylinder(20,15.0,15.0,center=false); 
}
translate([15,0,-2]) rotate([0,0,90]) intersection() {
translate([15.5884572681,0,0]) cylinder(80,18.0,18.0,center=false); 
rotate([0,0,180]) translate([15.5884572681,0,0]) cylinder(80,18.0,18.0,center=false); 
}
}
translate([0,-4,5]) cube([8,70,14],center=true); 
}
translate([0,0,-14]) translate([0,-4,5]) cube([8,70,14],center=true); 
}
translate([0,0,0]) union() {
union() {
translate([0,0,5]) rotate([90,0,0]) intersection() {
translate([8.66025403784,0,0]) cylinder(40,10,10,center=false); 
rotate([0,0,180]) translate([8.66025403784,0,0]) cylinder(40,10,10,center=false); 
}
translate([0,0,30]) intersection() {
translate([51.9615242271,0,0]) sphere(60); 
rotate([0,0,180]) translate([51.9615242271,0,0]) sphere(60); 
}
}
translate([20,0,30]) rotate([90,0,0]) rotate([0,90,0]) translate([0,0,-20]) intersection() {
translate([8.66025403784,0,0]) cylinder(20,10,10,center=false); 
rotate([0,0,180]) translate([8.66025403784,0,0]) cylinder(20,10,10,center=false); 
}
translate([15,0,30]) rotate([0,0,90]) intersection() {
translate([8.66025403784,0,0]) cylinder(50,10,10,center=false); 
rotate([0,0,180]) translate([8.66025403784,0,0]) cylinder(50,10,10,center=false); 
}
}
}
%cube([30,40,50]); 
}
