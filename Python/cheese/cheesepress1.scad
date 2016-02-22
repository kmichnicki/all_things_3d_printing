union() {
translate([0,0,50]) difference() {
cube([140,140,100],center=true); 
cube([130,130,200],center=true); 
}
union() {
translate([0,0,3.5]) cube([125,125,7],center=true); 
translate([0,0,15]) cylinder(30,20,20,center=true,$fs=0.02); 
}
}
