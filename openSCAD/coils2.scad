%cube([40,60,80]);
s1=1.5;

	
difference(){
		union(){
			translate([-s1*44,-10,0]) cube([s1*88,20,5]); 
			cylinder(5,14,14); 		
			for(i=[0:1]){
			rotate([0,0,i*180]) translate([s1*35,0,2]) cylinder(11,6.5,10);
			rotate([0,0,i*180]) translate([s1*35-13,0,2]) cylinder(11,6.5,10);
			}
}

cylinder(150,9,9);

}
		

	
