
//====================================================================//
//========================= layer0_proj.scad =========================//
//                                                                    //
// Autogenerated using py2scad. Hand editing this file is not         //
// advisable as all modifications will be lost when the program which //
// generated this file is re-run.                                     //
//====================================================================//

$fn = 100;
projection(cut=true) {
    difference() {
        cylinder(h=6.00000,r1=50.00000,r2=50.00000,center=true);
        translate(v=[39.40416, 22.75000, 0.00000]) {
            cylinder(h=24.00000,r1=1.11760,r2=1.11760,center=true);
        }
        translate(v=[0.00000, 45.50000, 0.00000]) {
            cylinder(h=24.00000,r1=1.11760,r2=1.11760,center=true);
        }
        translate(v=[-39.40416, 22.75000, 0.00000]) {
            cylinder(h=24.00000,r1=1.11760,r2=1.11760,center=true);
        }
        translate(v=[-39.40416, -22.75000, 0.00000]) {
            cylinder(h=24.00000,r1=1.11760,r2=1.11760,center=true);
        }
        translate(v=[-0.00000, -45.50000, 0.00000]) {
            cylinder(h=24.00000,r1=1.11760,r2=1.11760,center=true);
        }
        translate(v=[39.40416, -22.75000, 0.00000]) {
            cylinder(h=24.00000,r1=1.11760,r2=1.11760,center=true);
        }
    }
}

