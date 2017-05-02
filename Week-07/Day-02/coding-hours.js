'use strict';

// An average Green Fox attendee codes 6 hours daily
// The semester is 17 weeks long
//
// Print how many hours is spent with coding in a semester by an attendee,
// if the attendee only codes on workdays.
//
// Print the percentage of the coding hours in the semester if the average
// work hours weekly is 52

var attendee_daily = 6;
var weeks = 17;
var working_hours = 52;
var weekly_coding = 6*5;
var week_days = 5;

console.log("Coding hours per semester are " + attendee_daily * week_days * weeks + " hours.");
console.log("Coding hours are " + weekly_coding/working_hours * 100 + " percent of working hours.");
