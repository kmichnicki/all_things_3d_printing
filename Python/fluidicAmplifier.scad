difference() {
translate([0,0,2]) difference() {
difference() {
difference() {
cube([40,50,4],center=true); 
union() {
translate([27,-2,0]) cube([20,25.5,6],center=true); 
rotate([0,180,0]) translate([27,-2,0]) cube([20,25.5,6],center=true); 
} 
}
union() {
translate([13.5,-27,0]) cube([15,10,6],center=true); 
rotate([0,180,0]) translate([13.5,-27,0]) cube([15,10,6],center=true); 
}
}
union() {
translate([12,26,0]) cube([18,10,6],center=true); 
rotate([0,180,0]) translate([12,26,0]) cube([18,10,6],center=true); 
}
}
translate([0,0,2.01]) union() {
translate([0,-18,1]) cube([60,2,2],center=true); 
union() {
union() {
union() {
union() {
union() {
translate([5,0,0]) cylinder(2,10,10); 
rotate([0,0,180]) translate([5,0,0]) cylinder(2,10,10); 
}
translate([0,-18,0]) union() {
translate([1.5,0,0]) cylinder(2,4,4); 
rotate([0,0,180]) translate([1.5,0,0]) cylinder(2,4,4); 
}
}
translate([0,12,1]) union() {
translate([3,0,0]) rotate([0,0,30]) cube([16,6,2],center=true); 
rotate([0,180,0]) translate([3,0,0]) rotate([0,0,30]) cube([16,6,2],center=true); 
}
}
translate([0,0,1]) union() {
translate([16.3,15.6,0]) cube([16,6,2],center=true); 
rotate([0,180,0]) translate([16.3,15.6,0]) cube([16,6,2],center=true); 
}
}
union() {
union() {
translate([0,-6,1]) cube([6,40,2],center=true); 
translate([0,0,1]) union() {
translate([1,-13,0]) rotate([0,0,-12]) cube([6,10,2],center=true); 
rotate([0,180,0]) translate([1,-13,0]) rotate([0,0,-12]) cube([6,10,2],center=true); 
}
}
translate([0,15,1]) union() {
cube([1.5,25,2],center=true); 
cube([3,8,2],center=true); 
}
}
}
}
}
