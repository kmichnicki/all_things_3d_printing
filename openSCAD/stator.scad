%cube([40,60,80]);
s1=1.5;

	
difference(){
		union(){
			translate([-s1*42,-10,0]) cube([s1*84,20,5]); 
			//cylinder(5,14,14); 		
			
}
union(){
	for(i=[0:1]){
			rotate([0,0,i*180]) translate([s1*36,0,2]) cylinder(3,7,7);
			rotate([0,0,i*180]) translate([s1*35-14,0,2]) cylinder(3,7,7);
			}

	cylinder(150,3.5,3.5);
}
}
		

	
