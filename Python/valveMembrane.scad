scale(1.1) union() {
translate([0,0,12.5]) union() {
intersection() {
translate([0,0,8]) difference() {
rotate([0,90,0]) union() {
translate([0,50.25,-15]) difference() {
cylinder(30,50,50,$fn=50); 
cylinder(30,49,49,$fn=50); 
}
rotate([0,0,180]) translate([0,50.25,-15]) difference() {
cylinder(30,50,50,$fn=50); 
cylinder(30,49,49,$fn=50); 
}
}
translate([0,0,50]) cube([100,100,100],center=true); 
}
cube([30,10,25],center=true); 
}
difference() {
cube([30,10,25],center=true); 
cube([28,8,25],center=true); 
}
}
%cube(40,60,80); 
}
