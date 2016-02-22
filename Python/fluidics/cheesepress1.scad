union() {
difference() {
cube([140,140,100],center=true); 
cube([130,130,200],center=true); 
}
union() {
cube([125,125,7],center=true); 
cylinder(30,20,20,center=true,$fs=0.02); 
}
}
