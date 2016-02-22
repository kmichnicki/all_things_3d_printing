union() {
translate([0,0,20]) difference() {
union() {
intersection() {
union() {
difference() {
difference() {
cube([10,10,40],center=true); 
cube([8,8,40],center=true); 
}
translate([0,0,11]) rotate([60,0,0]) translate([0,0,50]) cube([100,100,100],center=true); 
}
translate([0,-8.5,0]) rotate([-28,0,0]) cube([12,1.2,50],center=true); 
}
translate([0,0,5]) cube([100,100,50],center=true); 
}
translate([0,-6,4]) difference() {
cube([16,28,48],center=true); 
translate([0,0,2]) cube([14,26,48],center=true); 
}
}
translate([0,0,-30]) cube([8,8,40],center=true); 
}
%cube([20,30,40]); 
}
