'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(a, b) {
    this.getArea = function () {
        console.log(a * b);
    };
    this.getCircumference = function () {
        console.log(2 * (a + b));
    };
}

var rectangle1 = new Rectangles(5,5);
rectangle1.getArea();
rectangle1.getCircumference();

var rectangle2 = new Rectangles(10,20);

rectangle2.getArea();
rectangle2.getCircumference();
