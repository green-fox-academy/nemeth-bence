'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

var x = 30;
var y = 40;
var z = 50;

console.log("Surface Area: " + (x+y + y+z + x+z));
console.log("Volume: " + (x*y*z));
