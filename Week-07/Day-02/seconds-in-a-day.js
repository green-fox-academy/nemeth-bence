
'use strict';

var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

var TotalDaySec = 24*60*60;
var Hours = 14*60*60;
var Mins = 34*60;
var Secs = 42;

console.log(TotalDaySec);
console.log(Hours);
console.log(Mins);

console.log("Remaining seconds from the day: " + (TotalDaySec - (Hours + Mins + Secs)));
