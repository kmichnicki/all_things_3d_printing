//%cube([40,60,80]);
s1=1.8;

difference(){
	union() {
		translate([0,0,70]) union() {
			linear_extrude(height = 140, center = true, convexity = 10, twist = -140)
			translate([s1*19,s1*0,s1*0]) difference() {circle(s1*20); circle(s1*19); translate([-s1*20,0,0]) square(s1*40,s1*20);}
			
			linear_extrude(height = 140, center = true, convexity = 10, twist = -140)
			rotate(0,0,180) translate([-s1*19,s1*0,s1*0]) difference() {circle(s1*19); circle(s1*18); translate([-s1*20,-s1*40,s1*0]) square(s1*40,s1*20);}
		}
		
		//cylinder(5,s1*40,s1*40);
		cylinder(140,6,6);
	}
	
		
			for(i=[0:5]){
			rotate([0,0,i*60]) translate([s1*32,0,0]) cylinder(3,7.5,7.5);
			}

			cylinder(150,3.5,3.5);
		

	

}