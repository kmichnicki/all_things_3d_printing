// *******************************************
// Self starting mapleseed experiment
// by Quentin Harley: (qharley)
// August 2011
// *******************************************

intersection(){
    cube(150);	
    translate([100,70,85])
	rotate([180,30,0]){
   		difference(){	
			intersection(){
				difference(){
					cylinder(100,100,0);
					cylinder(95,98,0);
					translate([-120,0,-55]){
						rotate([45,41,0])
							cube(200);
						}
				}
				translate([-50,73,0])
					cylinder(100,100,100);
			}
  			translate([0,90,0])
  			cylinder(100,80,80);  
   		}	
   		translate([0,0,90])
			sphere(12);	
	
	}
}