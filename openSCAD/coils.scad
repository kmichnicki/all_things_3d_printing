%cube([40,60,80]);
s1=1.5;

difference(){
union(){		
	cylinder(5,s1*40,s1*40);
				
	for(i=[0:5]){
	rotate([0,0,i*60]) translate([s1*32,0,5]) cylinder(6,7.5,10);
				}
}

cylinder(150,9,9);
}		

	

